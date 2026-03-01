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

# Space Complexity: O(2^N) – The algorithm generates all possible subsets of the
# input set. At each step, we are doubling the number of subsets we store. This
# means we are creating a new collection of subsets, where each subset
# potentially has a size of up to N (the number of elements in the input set).
# Therefore, the space required to store all 2^N subsets is proportional to N *
# 2^N in the worst case since each subset can have at most N elements. However,
# when considering space complexity, we usually focus on the number of subsets
# and ignore the size of each subset, so the space complexity is O(2^N).