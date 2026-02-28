class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# Time Complexity: O(n) – The algorithm involves three reversals of portions of the input array. Each reversal iterates through a section of the array, swapping elements from the start and end until the middle is reached. The first reversal processes all n elements. The second reversal processes k elements (where k is related to the rotation amount). The third reversal processes the remaining n-k elements. Since each reversal operation is linear with respect to the size of the portion it reverses, and the sum of the sizes of the portions is n, the overall time complexity is O(n).

# Space Complexity: O(1) – The algorithm operates by reversing sections of the input array in place. This involves swapping elements, which requires only a constant amount of extra space to hold temporary variables during the swap operation. No auxiliary data structures that scale with the input size N (where N is the number of elements in the array) are used. Therefore, the auxiliary space complexity is O(1).