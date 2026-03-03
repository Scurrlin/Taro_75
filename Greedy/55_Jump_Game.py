class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= maxJump:
                maxJump = i
        return maxJump == 0

# Time Complexity: O(n) – The algorithm iterates backward through the input
# array nums of size n, starting from the second-to-last element. For each
# element, it performs a constant-time check to see if it can reach the current
# destination. This check involves a single comparison: if nums[i] + i >=
# destination. The loop iterates n-1 times in the worst case, and each iteration
# involves a constant amount of work. Therefore, the total time complexity is
# O(n).

# Space Complexity: O(1) – The provided algorithm iterates backward through the
# input array, maintaining a single variable to track the current 'destination'
# index. No additional data structures, such as lists, hash maps, or recursion
# stacks, are used to store intermediate results or track visited elements.
# Therefore, the amount of auxiliary space remains constant regardless of the
# input array's size (N), resulting in O(1) space complexity.