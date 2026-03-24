class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

# Time Complexity: O(n + m) – The algorithm uses a two-pointer merge. At each
# step, the smaller of the two current nodes is appended to the result and its
# pointer advances. Each node from both lists is visited exactly once, so the
# total work is proportional to the combined length of the two lists.

# Space Complexity: O(1) – The algorithm re-links the existing nodes in-place
# rather than creating new ones. Only a dummy head node and a cursor pointer are
# allocated, giving constant auxiliary space regardless of input size.