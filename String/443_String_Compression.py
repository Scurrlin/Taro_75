class Solution:
    def compress(self, chars: List[str]) -> int:
        i, write = 0, 0
        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1
            chars[write] = ch
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1

        return write

# Time Complexity: O(n) – The algorithm iterates through the input string of
# length n exactly once. For each character, it performs a constant number of
# operations to count consecutive occurrences and append to the result. Even if
# the count is a multi-digit number, converting and appending it takes time
# proportional to the number of digits, which is logarithmic to the count
# itself, and the sum of all such logarithmic times across the string is still
# bounded by O(n). Thus, the total number of operations is directly proportional
# to the length of the string, resulting in O(n) time complexity.

# Space Complexity: O(1) – The algorithm iterates through the input string using
# a few variables to keep track of the current character and its consecutive
# count. No auxiliary data structures that grow with the input size N are
# created. The space used by these variables is constant, regardless of the
# string's length. Therefore, the auxiliary space complexity is O(1).
