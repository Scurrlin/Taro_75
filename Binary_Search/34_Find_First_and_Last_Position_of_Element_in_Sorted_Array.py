class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first, last = -1, -1
        l, r = 0, n - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                first = m
                r = m - 1

        if first == -1:
            return [-1, -1]

        l, r = first, n - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                last = m
                l = m + 1

        return [first, last]

# Time Complexity: O(log n) – The algorithm employs binary search to find both
# the first and last occurrences of the target value. Binary search repeatedly
# halves the search interval. Finding the first occurrence takes O(log n) time,
# and finding the last occurrence also takes O(log n) time. Since we perform two
# independent binary searches, the overall time complexity is O(log n) + O(log
# n), which simplifies to O(log n).

# Space Complexity: O(1) – The algorithm described uses a binary search
# approach, repeatedly dividing the search space in half. It only requires a few
# constant space variables to store the start, end, and middle indices for the
# search. The space used does not depend on the input size N (the number of
# elements in the sorted array). Therefore, the auxiliary space complexity is
# O(1).