class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# Time Complexity: O(n) – The algorithm iterates through each node of the linked
# list exactly once to reverse the pointers. The input size, n, represents the
# number of nodes in the linked list. For each node, a constant number of
# operations (pointer manipulation) is performed. Therefore, the total number of
# operations is directly proportional to the number of nodes, approximating n,
# which simplifies to O(n).

# Space Complexity: O(1) – The algorithm reverses the linked list in-place,
# meaning it modifies the existing list without creating new data structures
# that scale with the input size. It uses a few variables to keep track of the
# current node, the previous node, and the next node while changing the
# pointers. These variables consume a fixed amount of memory regardless of the
# number of nodes (N) in the linked list, hence the auxiliary space complexity
# is constant.
