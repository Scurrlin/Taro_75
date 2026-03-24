from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s)
        if max(counts.values()) > (n + 1)//2:
            return ""

        i = 0
        res = [""] * n
        for char, c in sorted(counts.items(), key=lambda x: -x[1]):
            for _ in range(c):
                if i >= n:
                    i = 1
                res[i] = char
                i += 2

        return "".join(res)

# Time Complexity: O(n) – Counting character frequencies with Counter takes
# O(n). Sorting the frequency items operates on at most 26 entries (fixed
# alphabet), which is O(1). Placing each of the n characters into the result
# array at alternating indices takes O(n). The dominant cost is the linear scan,
# so total time is O(n).

# Space Complexity: O(n) – The algorithm allocates a result list of size n
# (res = [""] * n) to build the rearranged string. The Counter and sorted list
# are bounded by the alphabet size (at most 26 entries), contributing O(1).
# Therefore, auxiliary space is O(n).