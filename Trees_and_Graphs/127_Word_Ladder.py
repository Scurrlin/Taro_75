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

# Time Complexity: O(M²N) – The time complexity is driven by the breadth-first
# search (BFS). In the worst case, we might need to explore all possible words.
# Let N be the number of words in the wordList and M be the length of each word.
# For each word in the queue (up to N words), we iterate through the entire
# wordList again to find one-letter-different words, which takes O(N) time.
# Finding one-letter-different words involves comparing each word which takes
# O(M) time. Thus, within the BFS loop, finding the neighbors dominates as
# O(M*N) in the worst case. Since we potentially explore each word, the overall
# complexity becomes O(M*N * N) or O(M*N²). The average word length (M) can be
# significant, so O(M * N^2) is a reasonable reflection of what drives the cost.

# Space Complexity: O(N) – The algorithm uses a queue to store words to explore,
# and in the worst-case scenario, the queue could contain all the words in the
# word list. The algorithm also modifies the original word list by removing
# visited words to prevent revisits which means, at worst, we iterate through
# all words. Let N be the number of words in the word list; therefore, the space
# complexity is dominated by the queue and the modified word list, leading to
# O(N) auxiliary space.
