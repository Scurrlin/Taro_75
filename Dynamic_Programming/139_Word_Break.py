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

# Time Complexity: O(n³) – The outer loop runs n times and the inner loop runs
# up to n times, giving O(n²) iterations. However, each iteration performs
# s[j:i], which creates a substring of length up to n in O(n) time, and the
# subsequent set lookup hashes that substring also in O(n) time. Therefore, each
# iteration costs up to O(n), and the total worst-case time is O(n² * n) =
# O(n³).

# Space Complexity: O(N) – The algorithm uses a data structure to remember which
# segments of the phrase are 'buildable'. This can be implemented using a
# boolean array or set, where each element corresponds to a position in the
# input string of length N, indicating whether the substring up to that position
# can be formed using words from the dictionary. Therefore, the auxiliary space
# used scales linearly with the length of the input string, N. In the worst
# case, we might need to store information for every prefix of the input string.