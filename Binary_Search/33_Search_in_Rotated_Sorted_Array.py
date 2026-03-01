class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# Time Complexity: O(log n) – The algorithm uses a modified binary search
# approach. In each step, the search space is halved by comparing the target
# value with the middle element and determining which half of the array to
# continue searching in. This halving of the search space continues until the
# target is found or the search space is exhausted. Therefore, the time
# complexity is logarithmic with respect to the input array size n, resulting in
# O(log n).

# Space Complexity: O(1) – The algorithm described operates using a binary
# search approach. It only requires storing a few variables to keep track of the
# start, end, and middle indices of the search range. These variables consume a
# constant amount of space, independent of the input array's size (N).
# Therefore, the auxiliary space complexity is O(1).