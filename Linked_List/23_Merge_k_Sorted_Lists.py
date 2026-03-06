class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

# Time Complexity: O(N log k) – Let k be the number of sorted lists, and N be
# the total number of elements across all lists. The algorithm repeatedly merges
# pairs of lists. In each merge step, we are effectively processing all N
# elements once. Since we are halving the number of lists in each step (like a
# binary tree), there are log k merge steps. Therefore, the total time
# complexity is O(N log k), where N is the total number of elements and k is the
# number of lists.

# Space Complexity: O(N) – The algorithm merges lists in pairs, creating new
# sorted lists. In the worst case, during intermediate merge steps, we may need
# to hold lists containing close to all N elements (where N is the total number
# of elements across all k lists) before the final merged list is constructed.
# The space is used to store the newly merged lists at each step. Therefore, the
# auxiliary space used is proportional to the total number of elements N,
# leading to a space complexity of O(N).