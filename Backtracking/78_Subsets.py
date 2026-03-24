class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(i):
            res.append(path.copy())
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return res

# Time Complexity: O(n * 2^n) – The algorithm iterates through each of the n
# elements in the input set. For each element, it effectively doubles the number
# of subsets accumulated so far. Since there are 2^n possible subsets in total,
# constructing each subset takes O(n) time (to copy the existing subset and
# potentially add the current element). Therefore, the overall time complexity
# is O(n * 2^n).

# Space Complexity: O(n * 2^n) – The output contains 2^n subsets, and the
# average subset size is n/2, so total output storage is O(n * 2^n). Excluding
# output, auxiliary space is O(n) for the recursion stack (max depth n) and the
# path list (max length n).