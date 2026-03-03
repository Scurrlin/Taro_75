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

# Time Complexity: O(2^n) – The described brute force approach explores every
# possible jump combination. In the worst case, from each position, we might be
# able to jump to almost every subsequent position. This creates a branching
# factor close to n at each step. Since there are n positions, the total number
# of possible jump paths grows exponentially, leading to approximately O(n^n)
# which is simplified by considering that there can only be jumps of maximum
# size to O(2^n).

# Space Complexity: O(N^N) – The brute force approach described explores every
# possible jump combination using recursion. In the worst-case, at each index,
# we could potentially try every possible jump length from 1 up to the maximum
# jump value at that index. This leads to a branching factor that is at worst
# proportional to N at each of the N possible positions, resulting in a
# recursion tree that can grow exponentially. The maximum depth of the recursion
# tree can be N, and at each level, the number of branches is also proportional
# to N, meaning that there are potentially N^N branches or call stack frames
# being held at a time. Therefore, the space complexity for the call stack
# becomes O(N^N).