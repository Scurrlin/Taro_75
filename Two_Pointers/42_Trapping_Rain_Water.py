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

# Time Complexity: O(n) – The algorithm iterates through the array of size n to
# find the maximum height to the left for each position. It then iterates
# through the array of size n again to find the maximum height to the right for
# each position. Finally, it iterates through the array of size n one more time
# to calculate the trapped water. Because these iterations are sequential (not
# nested) the time complexity is O(n) + O(n) + O(n), which simplifies to O(n).

# Space Complexity: O(N) – The algorithm creates two arrays, left_max and
# right_max, to store the maximum height to the left and right of each position,
# respectively. Both arrays have the same size as the input array, denoted as N.
# Therefore, the auxiliary space used is proportional to the input size N. This
# results in a space complexity of O(N).