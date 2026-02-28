class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        total = count = 0

        for n in nums:
            total += n
            count += freq.get(total - k, 0)
            freq[total] = freq.get(total, 0) + 1
        return count

# Time Complexity: O(n) – The algorithm makes a single pass through the array of size n. For each element, it performs constant-time operations: updating the running sum and checking/updating the hash map (freq), which are O(1) on average. Therefore, the total time complexity is O(n).

# Space Complexity: O(n) – The hash map (freq) stores prefix sums encountered during traversal. In the worst case, each prefix sum is unique, leading to up to n entries in the map. Thus, the auxiliary space grows linearly with the input size, resulting in O(n) space.