class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res

# Time Complexity: O(n) – We iterate through the array of temperatures once. For
# each temperature, we might perform a constant number of operations on a stack
# data structure. While the stack can grow up to size n, each element is pushed
# onto and popped from the stack at most once. Therefore, the total number of
# operations is proportional to the number of elements in the input array, n.
# This results in a linear time complexity of O(n).

# Space Complexity: O(n) – The solution uses a stack to keep track of the
# indices of days for which we haven't yet found a warmer day. In the worst-case
# scenario, if the temperatures are strictly decreasing, all N days' indices
# might be pushed onto the stack. Therefore, the auxiliary space complexity is
# directly proportional to the number of days, N, leading to O(n) space.