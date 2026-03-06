class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total//10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Time Complexity: O(max(m, n)) – The algorithm simulates manual addition by
# processing the digits of the two numbers one by one in a single pass. The
# process involves a single loop that continues until we have traversed all
# digits of both input numbers. Let the number of digits be m and n
# respectively; the total number of additions performed is determined by the
# length of the longer number. Therefore, the time complexity is directly
# proportional to the maximum of m and n, which simplifies to O(max(m, n)).

# Space Complexity: O(N) – The algorithm constructs a new sequence to store the
# result. The length of this new sequence is directly proportional to the length
# of the longer of the two input numbers. In the worst case, the result sequence
# will have N+1 digits, where N is the length of the longer input number.
# Therefore, the space required for the answer grows linearly with the size of
# the input, in addition to a single variable needed to keep track of the
# 'carry' value.
