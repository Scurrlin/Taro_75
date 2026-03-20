class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        cleaned = ''.join(chars)
        return cleaned == cleaned[::-1]

# Time Complexity: O(n) – The algorithm iterates through the input string with
# two pointers, one starting from the beginning and the other from the end,
# moving towards the middle. In the worst case, each pointer will traverse
# approximately half of the string's length. Each character comparison and skip
# operation takes constant time. Therefore, the total number of operations is
# directly proportional to the length of the string, n, leading to a time
# complexity of O(n).

# Space Complexity: O(1) – The solution uses a constant amount of extra space.
# This is because it only requires two pointers (variables) to track the start
# and end of the phrase, regardless of the input phrase's length. No additional
# data structures are created that grow with the input size N. Therefore, the
# auxiliary space complexity remains constant.