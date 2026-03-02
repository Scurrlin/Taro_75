class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

# Time Complexity: O(amount * n) – The algorithm iterates through each value
# from 1 up to the target amount (amount iterations). For each value, it loops
# through all coin denominations (n coins). Inside the inner loop, only constant-
# time operations are performed (comparison, subtraction, and assignment).
# Therefore, the total number of operations grows proportionally to amount * n.

# Space Complexity: O(amount) – The algorithm uses a one-dimensional DP array
# of size (amount + 1) to store the minimum number of coins needed for each
# sub-amount. No additional data structures are used, so the auxiliary space
# grows linearly with the input amount.