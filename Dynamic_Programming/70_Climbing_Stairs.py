class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 2, 1
        
        for _ in range(3, n + 1):
            current = one + two
            two = one
            one = current
        return one

# Time Complexity: O(n) – The solution calculates the number of ways to reach
# each step from 1 up to n. For each step, it performs a constant number of
# operations: a simple addition based on the results for the two preceding
# steps. Since we iterate through each step from 1 to n exactly once, the total
# number of operations is directly proportional to n. Therefore, the time
# complexity is O(n).

# Space Complexity: O(1) – The provided solution, as described by the pattern
# recognition and simple addition rule, only requires a constant number of
# variables to store the number of ways to reach the previous two steps. The
# input size N does not influence the number of additional variables used.
# Therefore, the auxiliary space complexity is constant.