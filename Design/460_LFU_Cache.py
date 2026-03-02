from typing import Optional, Dict


class Node:
    __slots__ = ("key", "val", "freq", "prev", "next")

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class DoublyLinkedList:
    __slots__ = ("head", "tail", "size")

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFront(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node
        self.size += 1

    def remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        self.size -= 1

    def popTail(self) -> Node:
        node = self.tail.prev
        self.remove(node)
        return node

    def isEmpty(self) -> bool:
        return self.size == 0

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 0
        self.keyToNode: Dict[int, Node] = {}
        self.freqToList: Dict[int, DoublyLinkedList] = {}

    def _touch(self, node: Node) -> None:
        oldFreq = node.freq
        self.freqToList[oldFreq].remove(node)

        if oldFreq == self.minFreq and self.freqToList[oldFreq].isEmpty():
            self.minFreq += 1
        node.freq += 1
        newFreq = node.freq

        if newFreq not in self.freqToList:
            self.freqToList[newFreq] = DoublyLinkedList()
        self.freqToList[newFreq].addFront(node)

    def get(self, key: int) -> int:
        node = self.keyToNode.get(key)
        if node is None:
            return -1
        self._touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        node = self.keyToNode.get(key)
        if node is not None:
            node.val = value
            self._touch(node)
            return

        if self.size == self.cap:
            lfuList = self.freqToList[self.minFreq]
            evicted = lfuList.popTail()
            del self.keyToNode[evicted.key]
            self.size -= 1

        newNode = Node(key, value)
        self.keyToNode[key] = newNode

        if 1 not in self.freqToList:
            self.freqToList[1] = DoublyLinkedList()
        self.freqToList[1].addFront(newNode)
        self.minFreq = 1
        self.size += 1

# Time Complexity: O(1) – The LFU cache operations described, get and put, rely
# on hash maps (dictionaries) and doubly linked lists. Hash map lookups and
# insertions are O(1) on average. Moving elements between frequency lists in the
# doubly linked list is also O(1). Therefore, the time complexity of both get
# and put operations is O(1), assuming hash collisions are minimal. Note that
# 'n' in this context would represent the cache capacity, but the operations are
# designed to be independent of the cache size.

# Space Complexity: O(N) – The solution uses a hash map to store the value and
# usage count for each item, which can grow up to the cache's capacity N. It
# also maintains a hash map to group items by their usage counts; in the worst
# case, each item has a unique usage count, leading to N entries. Therefore, the
# auxiliary space used is proportional to the cache's capacity, N, resulting in
# a space complexity of O(N).