class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
   
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

# Time Complexity: O(n) – The algorithm uses a greedy BFS-style approach with
# two pointers, l and r, representing the current reachable window. In each
# iteration, it scans from l to r to find the farthest reachable index, then
# shifts the window forward. Each element in the array is visited at most once
# across all iterations, so the total work is linear in the size of the input.

# Space Complexity: O(1) – The algorithm uses only a fixed number of scalar
# variables (l, r, res, maxJump) regardless of input size. No auxiliary data
# structures are allocated.