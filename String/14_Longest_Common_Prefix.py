class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pre = strs[0]

        for s in strs[1:]:
            i = 0
            while i < len(pre) and i < len(s) and pre[i] == s[i]:
                i += 1
            pre = pre[:i]
        return pre

# Time Complexity: O(S) – Let n be the number of strings in the input array and
# m be the length of the shortest string. In the described approach, we iterate
# through each string in the input array (n strings). For each string, we
# compare it character by character with the current shortest common prefix. In
# the worst case, we might compare up to m characters for each of the n strings.
# The total number of character comparisons is at most n * m, where m is the
# length of the shortest string. Therefore, the time complexity is proportional
# to the total number of characters in the input strings if we consider the sum
# of lengths of all strings, or more precisely, it's bounded by the number of
# strings multiplied by the length of the shortest string. Let S be the total
# number of characters across all strings. The algorithm effectively checks
# characters until a mismatch is found or the shortest string is exhausted. The
# total operations approximate S in the worst case, simplifying to O(S).

# Space Complexity: O(1) – The algorithm uses a constant amount of auxiliary space. It primarily relies on a few variables to store the current potential common prefix, its length, and loop indices. The size of these variables does not depend on the number of words (N) in the input list. Therefore, the extra memory usage remains constant regardless of the input size, resulting in O(1) space complexity.