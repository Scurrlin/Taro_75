class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

# Time Complexity: O(n) – The algorithm iterates through the Roman numeral
# string exactly once, from right to left. For each Roman numeral character, a
# constant time lookup is performed to get its integer value, and a constant
# time comparison and addition/subtraction operation is done. Therefore, if 'n'
# is the length of the Roman numeral string, the total number of operations is
# directly proportional to 'n', resulting in a time complexity of O(n).

# Space Complexity: O(1) – The algorithm primarily uses a single variable to
# maintain the running total and another variable to store the value of the
# previously processed Roman numeral. There are no auxiliary data structures
# that grow with the input string's length (N). The memory footprint remains
# constant regardless of the length of the Roman numeral string.