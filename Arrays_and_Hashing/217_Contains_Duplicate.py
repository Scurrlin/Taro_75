class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Time Complexity: O(n) – We iterate through the input array nums of size n
# once. For each number, we check if it exists in our "notebook" (a hash set in
# practice). Hash set lookups and insertions take constant time on average,
# O(1). Therefore, the dominant operation is iterating through the array once,
# which takes O(n) time. Thus, the overall time complexity is O(n).

# Space Complexity: O(N) – The provided solution uses a 'notebook' to remember
# numbers we've seen. This 'notebook' is essentially a data structure that
# stores elements from the input list. In the worst-case scenario, where all the
# elements in the input array are unique, the 'notebook' will store all N
# elements. Therefore, the auxiliary space required grows linearly with the
# input size N. This results in a space complexity of O(N).