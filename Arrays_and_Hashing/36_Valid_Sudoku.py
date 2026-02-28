class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": 
                    continue
                
                b = (r//3) * 3 + (c//3)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val); cols[c].add(val); boxes[b].add(val)
        
        return True

# Time Complexity: O(1) – The algorithm iterates through each row, column, and 3x3 subgrid of the Sudoku board. Because the Sudoku board has a fixed size (9x9), the number of operations performed is constant regardless of the numbers present in the board. The number of rows, columns and subgrids are fixed, leading to a fixed number of checks. Therefore, the time complexity is O(1).

# Space Complexity: O(1) – The algorithm checks rows, columns, and 3x3 squares for duplicates. To track the numbers seen in each row, column, or square, we can use a set or a similar data structure. Since the Sudoku board has fixed dimensions (9x9), the maximum size of these sets is limited by the number of possible values (1-9), which is constant. Therefore, the space used by these sets is constant regardless of the input, resulting in O(1) space complexity.