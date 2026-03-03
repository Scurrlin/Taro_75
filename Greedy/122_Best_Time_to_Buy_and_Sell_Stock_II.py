class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

# Time Complexity: O(n) – The solution iterates through the array of prices
# once, comparing each day's price with the next day's price. The number of
# iterations is directly proportional to the number of days, n, represented by
# the input array's size. Each comparison and potential profit calculation takes
# constant time. Therefore, the overall time complexity is linear with respect
# to the input size n.

# Space Complexity: O(1) – The provided strategy only involves iterating through
# the prices and accumulating profit. It doesn't require creating any additional
# data structures like arrays, hash maps, or trees to store intermediate results
# or track visited states. The space used is therefore independent of the input
# size, N, where N is the number of prices. The space complexity is constant
# because only a few variables (like the current profit) are used, regardless of
# how large the input array becomes.