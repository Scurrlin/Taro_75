class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n == 0 or m < n:
            return ""
        need, window = {}, {}

        for c in t:
            need[c] = 1 + need.get(c, 0)
        have, needCount = 0, len(need)
        best = [-1, -1]
        bestLen = float("inf")
        l = 0

        for r in range(m):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in need and window[c] == need[c]:
                have += 1
                
            while have == needCount:
                if r - l + 1 < bestLen:
                    best = [l, r]
                    bestLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l, r = best
        return s[l:r + 1] if bestLen != float("inf") else ""

# Time Complexity: O(m + n) – Let n be the length of the larger text (s) and m
# be the length of the set of required characters (t). Step 1 involves creating
# a frequency map of characters in t, which takes O(m) time. The core of the
# algorithm is the sliding window approach described in steps 2-5. The right
# pointer of the window iterates through the larger text at most n times, and
# the left pointer also iterates through the larger text at most n times in
# total across all shrinking operations. Each character check and frequency
# update within the window takes constant time (O(1)). Therefore, the combined
# operations of expanding and shrinking the window result in a linear traversal
# of the larger text, leading to a total time complexity of O(m + n).

# Space Complexity: O(1) – The algorithm uses a fixed number of hash maps to
# store character frequencies, and these hash maps can store at most the number
# of unique characters in the target string `t`. Since the number of unique
# characters is independent of the length of the input string `s`, the space
# used by these hash maps is constant. In addition, a few integer variables are
# used to track the window's start, end, and required character counts, but
# their space usage is also constant. Therefore, the overall auxiliary space
# complexity is O(1).