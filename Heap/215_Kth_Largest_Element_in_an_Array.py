# Optimal Solution (Quickselect + Dutch National Flag partitioning)

import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        l, r = 0, len(nums) - 1
        while True:
            pivot = nums[random.randint(l, r)]
            lt, i, gt = l, l, r

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1; i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                r = lt - 1
            elif target > gt:
                l = gt + 1
            else:
                return pivot

# Time Complexity: O(n) average / O(n²) worst-case - Quickselect examines
# progressively smaller partitions of the array. With randomized pivots, the
# expected work forms a geometric series (n + n/2 + n/4 + …), which sums to
# O(n). In the worst case, consistently poor pivots can produce highly
# unbalanced partitions, resulting in O(n²) time, though this is unlikely in
# practice.

# Space Complexity: O(1) - The algorithm operates in-place and uses an iterative
# loop rather than recursion, so it requires only constant extra space.

# Heap Solution

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]

# Time Complexity: O(n log k) – We maintain a min-heap of size k while scanning
# all n elements. The first k insertions cost O(k log k). For the remaining
# elements, each comparison is O(1), and any heap replacement costs O(log k).
# In the worst case, this results in O(n log k) time. If few replacements occur,
# the runtime approaches O(n).

# Space Complexity: O(k) – The heap stores at most k elements at any time.
# No recursion or additional data structures proportional to n are used,
# so the auxiliary space is O(k).