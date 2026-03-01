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

# Space Complexity: O(M*N) – The primary auxiliary space usage comes from the
# 'visited' set used to keep track of visited cells during the depth-first
# search, where M is the number of rows and N is the number of columns in the
# board. In the worst-case scenario, the recursive calls might explore almost
# all cells on the board, leading to a 'visited' set containing close to all
# board positions. Therefore the space complexity of the visited set would be
# O(M*N), since in worst case, we may visit all cells. The recursion depth will
# also be limited by the size of the board, contributing O(M*N) in the worst
# case, but this is accounted for in the visited set already.