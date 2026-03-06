class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

        res = ''
        vals = sorted(roman.keys(), reverse=True)

        for v in vals:
            while num >= v:
                res += roman[v]
                num -= v
        return res

# Time Complexity: O(1) – The algorithm iterates through a fixed-size table of
# integer-Roman numeral pairs. The size of this table is independent of the
# input integer n. The number of iterations is bounded by the number of entries
# in the table, which is constant. Therefore, the time complexity does not scale
# with the input and is O(1), constant time.

# Space Complexity: O(1) – The provided solution uses a table (which can be
# implemented as a constant-size array or hash map) to store integer-Roman
# numeral pairs. The size of this table is fixed regardless of the input integer
# N. The algorithm also uses a variable to store the resulting Roman numeral
# string. The length of the string depends on the integer, but the space
# allocated is bounded by a constant based on the largest representable integer
# (usually 3999). Therefore, the auxiliary space used is constant, independent
# of the input integer N.
