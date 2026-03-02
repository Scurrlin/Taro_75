class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

# Time Complexity: O(n) – The algorithm iterates through the input array of
# houses, `nums`, once. For each house, it performs a constant amount of work:
# comparing two values and updating a maximum value. Therefore, the time
# complexity is directly proportional to the number of houses, n, resulting in a
# linear time complexity of O(n).

# Space Complexity: O(1) – The algorithm keeps track of the maximum amount of
# money that can be robbed up to the current house by using a constant number of
# variables to store intermediate results (e.g., maximum robbed amount at the
# previous house, maximum robbed amount at two houses ago). The space required
# for these variables does not depend on the number of houses (N). Therefore,
# the space complexity is constant.