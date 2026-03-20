class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Time Complexity: O(m + n) – The algorithm iterates through the elements of
# both input arrays, nums1 (of effective length m) and nums2 (of length n),
# exactly once. The while loop continues as long as there are elements in either
# of the arrays to be considered. In the worst case, it checks all m elements of
# nums1 and all n elements of nums2 before completing, placing them into the
# merged array. Thus, the total number of operations is proportional to m + n,
# which simplifies to O(m + n).

# Space Complexity: O(1) – The algorithm operates in-place, modifying the first
# array directly. It uses only a few integer variables to keep track of the
# current positions in the arrays being merged. The number of variables does not
# depend on the size of the input arrays. Therefore, the space complexity is
# constant.