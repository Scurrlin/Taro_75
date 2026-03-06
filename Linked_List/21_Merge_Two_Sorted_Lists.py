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

# Time Complexity: O((n + m) log (n + m)) – The complexity is driven by the
# sorting step. Let n be the number of items in the first list and m be the
# number of items in the second. First, we iterate through both lists to create
# a combined collection of size (n + m), which takes O(n + m) time. The dominant
# operation is sorting this combined collection. A standard, efficient sorting
# algorithm has a time complexity of O(k log k), where k is the number of items.
# In this case, k equals (n + m), leading to a total time complexity of O((n +
# m) log (n + m)).

# Space Complexity: O(N) – The brute force strategy requires creating a new
# collection to hold all the elements from both input lists. If the first list
# has M elements and the second has L elements, this new collection will store M
# + L items, where N represents the total number of elements (M + L). The space
# required for this collection grows linearly with the total number of elements
# in the input lists, as it must hold a copy of every single item before
# sorting.