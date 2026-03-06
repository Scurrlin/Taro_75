from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res

# Time Complexity: O(n) – The time complexity is O(n) where n is the number of
# elements in the input array. Although there is an inner loop-like process to
# maintain the candidate list, each element from the input array is added to and
# removed from this list at most once over the entire algorithm. Therefore, the
# total number of operations for managing the candidate list is proportional to
# n. Since we iterate through the input array a single time, the total work is
# approximately n + n, which simplifies to O(n).

# Space Complexity: O(k) – The primary auxiliary space is used by the 'special
# list of candidates' described in the explanation. This list stores indices of
# elements from the input array, and its size is determined by the window size,
# k. In the worst-case scenario, where the elements in a window are in
# decreasing order, this list could hold up to k indices. Therefore, the space
# complexity is proportional to the window size, k, where N is the total number
# of elements in the input.