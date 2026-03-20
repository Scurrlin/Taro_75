class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

# Time Complexity: O(n) – The solution involves a single pass through the input
# array of size n. The 'sweeping marker' iterates through each of the n elements
# exactly once. For each non-zero element encountered, a constant number of
# operations (assignment and increment) are performed. Therefore, the total
# number of operations is directly proportional to the number of elements, n.
# This leads to a linear time complexity of O(n).

# Space Complexity: O(1) – The provided solution rearranges the elements
# in-place within the original array. It only utilizes a few constant-size
# variables to keep track of marker positions. These variables do not depend on
# the size of the input array, N. Therefore, the auxiliary space complexity is
# constant, O(1).