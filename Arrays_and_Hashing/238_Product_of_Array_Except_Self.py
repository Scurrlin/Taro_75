class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res

# Time Complexity: O(n) – The algorithm makes two passes through the input array of size n. The first loop computes prefix products, and the second loop computes suffix products while updating the result array. Each loop runs in O(n) time, and all operations inside the loops are O(1). Since the loops are sequential (not nested), the total time complexity is O(n).

# Space Complexity: O(1) – The solution uses a result array to store the output, which is not counted as extra space according to the problem constraints. Aside from this, only two variables ('pre' and 'suf') are used to store running products. No additional data structures are used, and the extra space does not grow with input size. Therefore, the auxiliary space complexity is O(1).