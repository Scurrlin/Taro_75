class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# Time Complexity: O(n) – The algorithm iterates through the array of children's
# ratings twice. The first loop traverses from left to right to adjust candy
# counts based on the left neighbor's rating. The second loop goes from right to
# left, adjusting candy counts based on the right neighbor's rating while
# ensuring we keep the maximum candies assigned. Both loops visit each of the n
# children once. Therefore, the time complexity is proportional to the number of
# children, resulting in O(n).

# Space Complexity: O(N) – The algorithm uses an auxiliary array called
# 'candies' to store the number of candies allocated to each child. This array
# has the same length as the input array 'ratings', where N represents the
# number of children (and the length of the ratings array). Therefore, the space
# required by the 'candies' array grows linearly with the input size N. No other
# significant auxiliary data structures are used.