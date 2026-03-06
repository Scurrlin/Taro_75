class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bot = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        while top <= bot and l <= r:

            for col in range(l, r + 1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bot + 1):
                res.append(matrix[row][r])
            r -= 1

            if top <= bot:
                for col in range(r, l - 1, -1):
                    res.append(matrix[bot][col])
                bot -= 1

            if l <= r:
                for row in range(bot, top - 1, -1):
                    res.append(matrix[row][l])
                l += 1

        return res

# Time Complexity: O(m * n) – The algorithm processes the matrix by peeling off
# layers until all elements are visited. In the worst case, every element in the
# matrix is visited exactly once. If the matrix dimensions are m rows and n
# columns, the algorithm visits m * n elements. Therefore, the time complexity
# is directly proportional to the total number of elements in the matrix,
# resulting in O(m * n).

# Space Complexity: O(1) – The provided algorithm traverses the matrix in place,
# modifying only the boundaries for iteration. It doesn't create any auxiliary
# data structures like lists, sets, or maps to store intermediate results or
# visited elements. The space used is limited to a few integer variables to
# track the current boundaries or indices of the matrix, which remains constant
# irrespective of the input matrix's dimensions (N). Therefore, the space
# complexity is O(1).