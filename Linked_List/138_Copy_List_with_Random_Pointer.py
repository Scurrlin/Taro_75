class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = {}
        curr = head

        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            copy[curr].next = copy.get(curr.next)
            copy[curr].random = copy.get(curr.random)
            curr = curr.next

        return copy[head]

# Time Complexity: O(n) – The algorithm makes two sequential passes over the
# linked list of n nodes. The first pass creates a clone of every node and
# stores the original-to-clone mapping in a hash map, each insertion being O(1).
# The second pass wires up the next and random pointers on each clone using O(1)
# hash map lookups. Total work is O(n) + O(n) = O(n).

# Space Complexity: O(n) – A hash map (dictionary) is used to store a mapping
# from every original node to its corresponding clone. With n nodes in the list,
# the map holds n key-value pairs, so auxiliary space grows linearly with n.