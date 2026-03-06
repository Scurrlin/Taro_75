class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0

        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10

# Time Complexity: O(log10(n)) – The complexity is determined by the number of
# digits in the input integer, which we can call 'n'. The solution's core logic
# is a single while loop that processes the number by repeatedly dividing it by
# 10. This division effectively removes one digit in each iteration. The loop
# runs until half of the digits are processed. Therefore, the number of
# operations is proportional to the number of digits in n, which is
# mathematically represented as log base 10 of n. This means the total
# operations approximate log10(n) / 2, which simplifies to O(log10(n)).

# Space Complexity: O(1) – The algorithm uses a fixed number of integer
# variables to store the reversed half of the number and for intermediate
# calculations. This memory usage does not scale with the number of digits in
# the input integer, N. Because the amount of auxiliary space required is
# constant regardless of the input's size, the space complexity is constant.