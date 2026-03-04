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

# Time Complexity: O(n log n) – Counting character frequencies involves
# iterating through the string of length n, taking O(n) time. Prioritizing
# characters based on frequency typically uses a heap-based priority queue.
# Inserting each of the up to n distinct characters into the heap takes O(log n)
# time, and we do this up to n times resulting in O(n log n) for heap
# operations. Building the reorganized string involves placing each of the n
# characters at the correct index. Thus, the dominant operation is the heap
# operations resulting in a time complexity of O(n log n).

# Space Complexity: O(1) – The algorithm uses a character frequency count,
# which, assuming a fixed character set (e.g., ASCII), requires constant space.
# The rearranged string is built in-place (or implicitly using a fixed-size
# output buffer), so it doesn't contribute to auxiliary space. Therefore, the
# space complexity remains constant regardless of the input string length, N.