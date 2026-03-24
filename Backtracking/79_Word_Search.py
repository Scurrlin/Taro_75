class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            char = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1))
            board[r][c] = char
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False

# Time Complexity: O(M * N * 4^L) – Let M be the number of rows and N be the
# number of columns in the board, and L be the length of the word. The algorithm
# iterates through each cell in the M x N board, giving us M * N starting
# points. From each starting point, we explore at most 4 possible directions
# (up, down, left, right) for each letter in the word. In the worst-case
# scenario, we might explore almost every possible path of length L from each
# starting cell before either finding the word or exhausting all possibilities.
# This leads to a branching factor of 4 for each of the L letters in the word,
# hence 4^L. Therefore, the total time complexity is approximately M * N * 4^L.

# Space Complexity: O(L) – where L is the length of the word. No separate
# visited set is used; instead, the board is modified in-place by temporarily
# replacing visited cells with '#' and restoring them after backtracking. The
# only auxiliary space is the recursion call stack, whose maximum depth equals
# the word length L (one frame per matched character).