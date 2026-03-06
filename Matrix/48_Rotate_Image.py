class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

# Time Complexity: O(n²) – The first step involves traversing the upper triangle
# of the n x n matrix to flip it across the main diagonal. This requires
# visiting approximately n * n / 2 elements. The second step requires flipping
# the matrix horizontally. This iterates through each row (n rows) and swaps
# elements from the start and end until the middle is reached (n/2 swaps per
# row). Thus, n * n/2 operations are required in the second step. Overall,
# approximately n * n / 2 + n * n / 2 operations are performed, which simplifies
# to O(n²).

# Space Complexity: O(1) – The algorithm performs in-place transformations,
# flipping the image across the main diagonal and then horizontally. These
# operations involve swapping elements within the existing matrix, without
# allocating any new data structures to store intermediate results.
# Consequently, the amount of auxiliary space used remains constant, independent
# of the image size N, where N is the number of rows (or columns) in the square
# matrix. Thus, the space complexity is O(1).