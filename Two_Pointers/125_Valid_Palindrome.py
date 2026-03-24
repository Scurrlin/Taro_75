class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        cleaned = ''.join(chars)
        return cleaned == cleaned[::-1]

# Time Complexity: O(n) – The algorithm makes one pass through the string of
# length n to filter alphanumeric characters into a list, then joins them into a
# cleaned string and creates a reversed copy. Each of these operations is O(n),
# and since they are sequential the total time is O(n).

# Space Complexity: O(n) – The algorithm builds a list of up to n characters,
# joins them into a new string of up to length n, and creates a reversed copy of
# that string. These three auxiliary data structures each use space proportional
# to n, so the total auxiliary space is O(n).