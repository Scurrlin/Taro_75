from typing import Optional

class Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def addFront(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def moveToFront(self, node: Node) -> None:
        self.remove(node)
        self.addFront(node)

    def popLRU(self) -> Node:
        lru = self.tail.prev
        self.remove(lru)
        return lru

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.val = value
            self.moveToFront(node)
            return

        if len(self.cache) == self.cap:
            lru = self.popLRU()
            del self.cache[lru.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.addFront(new_node)

# Time Complexity: O(1) – The solution uses a hash map for the quick-access
# directory and a doubly linked list for the usage order. The `get` operation
# involves a hash map lookup and moving a node to the front of the list, both of
# which are constant time operations. The `put` operation also consists of
# constant time steps: a hash map lookup, potentially removing the last node
# (tail) from the list, adding a new node to the front (head), and updating the
# hash map. Since every action is performed in a fixed number of steps
# regardless of the cache's capacity, the time complexity for both `get` and
# `put` is O(1).

# Space Complexity: O(C) – The space complexity is determined by the two core
# data structures used to implement the cache. We use a 'quick-access
# directory', which is a hash map, and a 'single line' representing usage order,
# implemented as a doubly linked list. Both of these structures will store at
# most a number of elements equal to the cache's capacity, which we can denote
# as C. Therefore, the total auxiliary space required grows linearly with the
# capacity of the cache.