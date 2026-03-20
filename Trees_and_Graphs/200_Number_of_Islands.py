class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(row, col):
            if not (0 <= row < rows 
                and 0 <= col < cols
                and grid[row][col] == '1'):
                return
            
            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
        
        return islands

# Time Complexity: O(m * n) – Let m be the number of rows and n be the number of
# columns in the grid. The algorithm iterates through each cell of the grid
# once. When a land cell ('1') is found, a Depth First Search (DFS) or Breadth
# First Search (BFS) is initiated. This search visits each connected land cell
# exactly once, marking it as visited (or sinking it). In the worst case, every
# cell could be part of a single island or multiple islands. Since each cell is
# visited at most a constant number of times (once by the outer loop and at most
# once by a DFS/BFS traversal), the total time complexity is proportional to the
# total number of cells in the grid, which is m * n.

# Space Complexity: O(M*N) – The primary contributor to auxiliary space
# complexity is the recursion stack when exploring connected land masses. In the
# worst-case scenario, where the entire grid is a single island, the recursion
# depth can be proportional to the total number of cells in the grid. If the
# grid has M rows and N columns, the recursion stack could grow up to O(M*N) in
# depth, representing the maximum number of function calls. Therefore, the
# auxiliary space complexity is dominated by this recursion stack and is O(M*N).