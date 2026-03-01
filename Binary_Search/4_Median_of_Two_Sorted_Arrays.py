class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1)//2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi)//2
            j = half - i

            l1 = nums1[i - 1] if i else float("-inf")
            l2 = nums2[j - 1] if j else float("-inf")
            r1 = nums1[i] if i < m else float("inf")
            r2 = nums2[j] if j < n else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0

            if l1 > r2:
                hi = i - 1
            else:
                lo = i + 1

        raise ValueError()

# Time Complexity: O(log(min(m, n))) – The algorithm performs a binary search on
# the shorter of the two arrays. Let m and n represent the lengths of the two
# arrays. In each step of the binary search, the search space is halved. The
# cost is driven by the binary search on the shorter array which results in
# log(min(m, n)) iterations. Therefore, the time complexity is O(log(min(m,
# n))).

# Space Complexity: O(1) – The provided algorithm iteratively narrows down the
# search range using comparisons and adjustments of cut points (index
# variables). It does not create any auxiliary data structures like lists,
# arrays, or hash maps to store intermediate results or track visited elements.
# The operations involve only a few integer variables to keep track of the cut
# positions. Therefore, the auxiliary space used is constant and independent of
# the input size, resulting in O(1) space complexity.