# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

# Time Complexity: O(n) – The algorithm makes a single pass through the array.
# At each step, it performs constant-time operations (addition, comparison,
# and assignment). Therefore, the total time grows linearly with the number
# of elements in the input array.

# Space Complexity: O(1) – The algorithm uses a fixed number of variables
# (e.g., current_max / total and overall_max / res) regardless of input size.
# No additional data structures are used, so the auxiliary space remains constant.