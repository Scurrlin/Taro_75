class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        best = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                best = max(best, p - minPrice)
        return best

# Time Complexity: O(n) – The algorithm iterates through the list of stock
# prices exactly once. For each of the 'n' days (elements in the input array),
# we perform a constant number of operations: comparing the current price to the
# minimum price seen so far, calculating a potential profit, and updating the
# maximum profit if necessary. Since we only traverse the array one time, the
# total number of operations is directly proportional to the number of elements,
# 'n'. Therefore, the time complexity is O(n).

# Space Complexity: O(1) – The solution requires only a constant amount of extra
# memory, regardless of the input size N. This is because we only need to store
# two variables: one to keep track of the lowest price seen so far ('best buying
# opportunity') and another to store the greatest profit found so far ('greatest
# possible profit'). The number of these variables does not change with the
# number of days (N) in the stock price list.