class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res

# Time Complexity: O(log n) – The dominant operation in this algorithm is
# repeatedly halving the exponent n in each iteration of the loop. Each division
# by 2 brings the exponent closer to zero. The number of times the exponent can
# be halved before reaching zero is logarithmic with respect to the initial
# value of n. Therefore, the time complexity is O(log n).

# Space Complexity: O(1) – The algorithm uses a constant amount of extra space.
# It stores a few variables to keep track of the base, exponent, and the
# intermediate result. The space required by these variables does not depend on
# the size of the exponent (n) or the base (x). Therefore, the auxiliary space
# complexity is O(1).