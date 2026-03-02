# Manacher's Algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        center = right = 0
        maxLen = maxCenter = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
            if p[i] > maxLen:
                maxLen = p[i]
                maxCenter = i

        start = (maxCenter - maxLen)//2
        return s[start : start + maxLen]

# Time Complexity: O(n) – The algorithm processes a transformed version of the
# string where separators are inserted between characters to unify handling of
# even and odd length palindromes. It maintains a center and right boundary to
# reuse previously computed palindrome information via symmetry (mirror
# indices). Each character is processed in constant time on average, and while
# expansion may occur, the total number of expansions across the entire string
# is linear. Therefore, the overall time complexity is O(n).

# Space Complexity: O(n) – The algorithm constructs a transformed string of size
# approximately 2n + 3 and uses an auxiliary array to store palindrome radii at
# each position. Both the transformed string and the array require linear space
# proportional to the input size. Hence, the auxiliary space complexity is O(n).