from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque([(beginWord, 1)])
        if endWord not in words:
            return 0
        
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in range(26):
                    next = word[:i] + chr(ord('a') + c) + word[i+1:]
                    if next in words:
                        words.remove(next)
                        q.append((next, steps + 1))

        return 0

# Time Complexity: O(M² * N) – Let N be the number of words in the wordList and
# M be the length of each word. BFS dequeues up to N words. For each word, we
# try M positions and 26 letter substitutions. At each position, building the
# candidate string via slicing costs O(M), and the subsequent set membership
# check (hashing the string) also costs O(M). This gives O(M * 26 * M) = O(M²)
# work per word, and O(M² * N) total across all words dequeued.

# Space Complexity: O(M * N) – The words set stores up to N strings each of
# length M, using O(M * N) space. The BFS queue can also hold up to N words of
# length M. Therefore, total auxiliary space is O(M * N).
