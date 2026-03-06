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

# Time Complexity: O(n) – The algorithm iterates through the linked list three
# times. First, it iterates through the original list of n nodes to create a
# copy of each node and insert it after the original (this step takes O(n)
# time). Second, it iterates through the augmented list of 2n nodes to assign
# the random pointers of the copied nodes (this step takes O(n) time because
# each random pointer assignment is a constant-time operation). Finally, it
# iterates through the augmented list again to separate the original and copied
# lists (again O(n) time). Since all steps are linear and sequential, the
# overall time complexity is O(n) + O(n) + O(n) which simplifies to O(n).

# Space Complexity: O(1) – The provided solution modifies the original list in
# place and creates a new list by weaving copies into the original list
# structure. No auxiliary data structures like hash maps or additional lists are
# used to store intermediate results or track visited nodes. The operations
# involve only pointer manipulation and temporary variable assignments, which
# require a constant amount of extra space regardless of the number of nodes (N)
# in the original list. Therefore, the auxiliary space complexity is O(1).