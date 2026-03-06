class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# Time Complexity: O(n) – The algorithm consists of scanning the input array of
# size n from right to left to find the first element that is smaller than its
# right neighbor, taking O(n) time. Next, another scan from right to left is
# performed to find the smallest element larger than the previously found
# element, again taking O(n) time. Then, these two elements are swapped, an O(1)
# operation. Finally, the subarray to the right of the first element found is
# reversed, which takes O(n) time. Since all operations are at most linear, the
# overall time complexity is O(n).

# Space Complexity: O(1) – The algorithm operates in place, modifying the input
# array directly. It uses a few index variables to track positions during the
# search and swapping operations. These variables require constant space,
# independent of the size of the input array, denoted as N. Therefore, the
# auxiliary space complexity is O(1).