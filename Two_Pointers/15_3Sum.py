class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res

# Time Complexity: O(n²) – The algorithm begins by sorting the input array of
# size n, which takes O(n log n) time. After sorting, the algorithm iterates
# through each element of the sorted array (outer loop - n iterations). For each
# element, a two-pointer approach is used on the remaining part of the array
# which requires at most n comparisons in the worst case (inner while loop).
# Thus, the dominant operation involves the nested loop structure that
# approximates n * n/2 operations. Therefore the time complexity is O(n²), as we
# drop the n log n from sorting and the constant factor of 1/2.

# Space Complexity: O(1) – The algorithm primarily sorts the input array
# in-place, and uses a fixed number of integer variables for pointers and sums.
# The recorded triplets are stored in a list; however, the problem statement
# does not explicitly mention constraints on the number of triplets. If we
# assume a constant number of triplets can be stored, then the space needed
# remains constant regardless of the input size N. Therefore, the auxiliary
# space complexity is O(1).