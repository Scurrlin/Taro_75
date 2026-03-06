class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res

# Time Complexity: O(n) – The algorithm iterates through the input string of
# length n once. Each character is visited by the right pointer of the sliding
# window at most once, and by the left pointer of the sliding window at most
# once. Operations within the loop, such as checking for character existence in
# a set or map and updating the window boundaries, take amortized constant time.
# Therefore, the total time complexity is linear with respect to the input size
# n.

# Space Complexity: O(min(n, m)) – The algorithm uses a data structure,
# typically a hash map or a set, to keep track of characters within the current
# sliding window. In the worst case, this structure will store all unique
# characters present in the input string. If the alphabet size (m) is smaller
# than the string length (n), the space used is bounded by O(m). Otherwise, it's
# bounded by O(n). Therefore, the auxiliary space complexity is O(min(n, m)),
# where n is the length of the input string and m is the size of the character
# set.