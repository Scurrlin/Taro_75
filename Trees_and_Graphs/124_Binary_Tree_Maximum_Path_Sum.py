class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            res[0] = max(res[0], root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return res[0]

# Time Complexity: O(n) – The algorithm performs a single Depth-First Search
# (DFS) traversal of the binary tree. Each node in the tree is visited exactly
# once. At each node, a constant amount of work is done: calculating the maximum
# path sum including the node and updating the global maximum. Therefore, the
# time complexity is directly proportional to the number of nodes in the tree,
# which is denoted as 'n'. This single traversal leads to a linear relationship
# between the number of nodes and the execution time.

# Space Complexity: O(H) – The dominant space complexity comes from the
# recursion depth of the depth-first traversal. In the worst case, the tree is
# skewed, and the recursion depth equals the height of the tree, H, leading to H
# stack frames. Each stack frame stores local variables for the current node
# being processed and the return address. Therefore, the auxiliary space used is
# proportional to the height of the tree. In the best/average case for a
# balanced tree the height is log(N) but the question asks for the generic case
# space complexity analysis so we will consider H which is the height of the
# tree as our result.