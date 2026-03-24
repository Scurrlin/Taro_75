class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        if not h:
            return 0
        l, r = 0, len(h) - 1
        leftMax, rightMax, volume = h[l], h[r], 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, h[l])
                volume += leftMax - h[l]
            else:
                r -= 1
                rightMax = max(rightMax, h[r])
                volume += rightMax - h[r]
        return volume

# Time Complexity: O(n) – Two pointers start at opposite ends of the array and
# converge toward the middle. Each iteration advances one pointer, so at most n
# steps are taken before the pointers meet. Each step does constant work
# (comparison, max update, addition), giving O(n) total time.

# Space Complexity: O(1) – The algorithm tracks only a fixed number of scalar
# variables (l, r, leftMax, rightMax, volume). No auxiliary arrays or data
# structures are allocated, so space usage is constant regardless of input size.