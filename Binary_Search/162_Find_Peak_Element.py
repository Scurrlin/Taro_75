class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

# Time Complexity: O(log n) – The algorithm employs a binary search approach.
# With each step, the search space is halved. We start with an input array of
# size n, and in each iteration, we reduce the problem size by half, checking
# only the middle element and its neighbors. This halving continues until we
# find a peak element. The number of iterations required to reduce the problem
# to a constant size is logarithmic with base 2, therefore the time complexity
# is O(log n).

# Space Complexity: O(1) – The algorithm is purely iterative, using a while loop
# with two index variables (l and r) and a computed midpoint. No recursion or
# auxiliary data structures are used, so space is constant regardless of input
# size.