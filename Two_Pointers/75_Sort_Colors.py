class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, l, r = 0, 0, len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1

# Time Complexity: O(n) – The time complexity is determined by the number of
# times we inspect an element in the input array of size n. The provided
# single-pass approach uses a pointer to traverse the 'unknown' section of the
# array. This pointer starts at the beginning and moves towards the end, with
# each element being examined exactly once before it is placed in its correct
# section (red, white, or blue). Since every element is visited and processed a
# constant number of times, the total number of operations is directly
# proportional to n. Therefore, the algorithm has a linear time complexity,
# which simplifies to O(n).

# Space Complexity: O(1) – The algorithm sorts the array in-place, meaning it
# rearranges the elements within the original array without creating any new
# data structures. It only requires a few variables to keep track of the
# boundaries of the red, white, and blue sections. Since the number of these
# pointer variables does not change regardless of the input array's size (N),
# the auxiliary space complexity is constant.