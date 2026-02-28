class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

# Time Complexity: O(n) – This solution implements the Boyer–Moore Voting Algorithm, which processes the input array in a single pass. For each of the n elements, it performs a constant amount of work: checking whether the count is zero, potentially updating the current candidate, and incrementing or decrementing the count. All of these operations run in O(1) time. Since each element is visited exactly once, the overall time complexity is O(n).

# Space Complexity: O(1) – The algorithm uses only two variables: 'res' to store the current candidate for the majority element, and 'count' to track its relative frequency. No additional data structures are used, and the amount of memory required does not depend on the size of the input array. Therefore, the space complexity is constant, resulting in O(1).