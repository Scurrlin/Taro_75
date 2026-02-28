class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x], i]
            seen[num] = i

# Time Complexity: O(n) - We iterate through the input list of size n exactly once. For each element, we perform a constant time lookup in a hash map (or dictionary) to check for the complement. Since we only traverse the list once and each operation within the loop takes constant time, the total time complexity is directly proportional to the number of elements, n. This results in a runtime of O(n).
 
# Space Complexity: O(n) - The solution uses a hash map (or similar dictionary-like structure) to store numbers encountered so far along with their indices. In the worst-case scenario, where no pair sums to the target until the very last element is processed, all N elements of the input list might be stored in this hash map. Therefore, the auxiliary space complexity is directly proportional to the number of elements in the input list, denoted as N. This leads to a space complexity of O(n).