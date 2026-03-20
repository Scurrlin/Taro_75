class Solution:
    def maxArea(self, height: List[int]) -> int:
        h, maxArea = height, 0
        l, r = 0, len(h) - 1

        while l < r:
            if h[l] < h[r]:
                area = h[l] * (r - l)
                l += 1
            else:
                area = h[r] * (r - l)
                r -= 1
            maxArea = max(maxArea, area)
        return maxArea

# Time Complexity: O(n) – The algorithm uses two pointers, one starting at the
# beginning of the array (left) and one at the end (right). In each step, we
# calculate the water capacity and then move either the left pointer or the
# right pointer inwards. Since in each iteration, at least one of the pointers
# moves one step closer to the other, and they start at opposite ends of an
# array of size n, the process will terminate when the pointers meet. This means
# we perform a constant amount of work for each of the n steps, resulting in a
# linear time complexity of O(n).

# Space Complexity: O(1) – The provided solution utilizes a constant amount of
# extra memory. It only requires a few integer variables to keep track of the
# left pointer, right pointer, and the maximum water encountered so far. The
# space usage does not grow with the input size, denoted as N, representing the
# number of bars. Therefore, the auxiliary space complexity is constant.