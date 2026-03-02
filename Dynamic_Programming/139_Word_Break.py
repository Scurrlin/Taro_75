class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]

# Time Complexity: O(n²) – The algorithm iterates through all possible prefixes
# of the input string of length n, which takes O(n) time. For each prefix, it
# iterates through the dictionary to check if a word exists that can extend the
# prefix to a valid word sequence. In the worst case, the inner loop iterates
# through the entire dictionary for each prefix, and the dictionary lookup can
# take O(1) time (assuming a hash set). Additionally, within the outer loop, we
# also have an inner loop that implicitly checks all possible starting points of
# the words that make up the string, which will also be O(n) at the most. This
# results in a nested loop structure where we do work that approximates n * n/2
# operations, leading to a time complexity of O(n²).

# Space Complexity: O(N) – The algorithm uses a data structure to remember which
# segments of the phrase are 'buildable'. This can be implemented using a
# boolean array or set, where each element corresponds to a position in the
# input string of length N, indicating whether the substring up to that position
# can be formed using words from the dictionary. Therefore, the auxiliary space
# used scales linearly with the length of the input string, N. In the worst
# case, we might need to store information for every prefix of the input string.