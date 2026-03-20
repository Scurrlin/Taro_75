from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1
        return time if fresh == 0 else -1

# Time Complexity: O(M * N) – Let M be the number of rows and N be the number of
# columns in the grid representing the oranges. Each orange cell is visited and
# processed at most a constant number of times. We initially scan the grid to
# find fresh and rotten oranges, taking O(M * N) time. Then, we use a
# Breadth-First Search (BFS) approach, processing each orange cell once when it
# becomes rotten. In the worst case, every cell might become rotten and be added
# to the queue. The BFS queue operations (enqueue and dequeue) and neighbor
# checks take constant time per cell. Therefore, the total time complexity is
# dominated by visiting each cell at most a few times, resulting in O(M * N).

# Space Complexity: O(R*C) – The primary auxiliary data structure used is a
# queue to store the coordinates of rotten oranges that will spread the rot. In
# the worst case, all R*C cells in the grid could be added to the queue
# simultaneously if they are initially rotten or become rotten in the first time
# step. Therefore, the space complexity is proportional to the total number of
# cells in the grid, denoted as N, where N = R*C. This results in a space
# complexity of O(N) or O(R*C).