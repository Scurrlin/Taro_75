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

# Space Complexity: O(log N) – The algorithm employs a binary search approach,
# repeatedly halving the search space. This halving is achieved through
# recursive calls (or an iterative equivalent using a stack). Each recursive
# call adds a new frame to the call stack, storing local variables like the
# middle index. In the worst-case scenario, the recursion depth (or stack size)
# is proportional to the number of times N can be divided by 2 before reaching
# 1, which is log2(N). Therefore, the space used by the recursion stack grows
# logarithmically with the input size N, resulting in O(log N) space complexity.