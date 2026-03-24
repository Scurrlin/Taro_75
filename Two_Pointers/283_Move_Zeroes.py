class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

# Time Complexity: O(n) – A single pass is made through the array of size n.
# The right pointer visits every element exactly once, and each swap is a
# constant-time operation. Therefore, the total work is linear in n.

# Space Complexity: O(1) – The algorithm rearranges elements in-place using only
# two pointer variables (l and r). No auxiliary data structures are allocated, so
# the space usage is constant regardless of input size.
