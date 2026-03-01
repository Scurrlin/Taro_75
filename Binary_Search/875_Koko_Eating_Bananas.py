class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            hours = 0
            for p in piles:
                hours += (p + m - 1)//m
            if hours <= h:
                r = m
            else:
                l = m + 1

        return l
    
# Time Complexity: O(n log m) – The algorithm uses binary search to find the
# optimal eating speed. The search space for the eating speed ranges from 1 to
# the maximum number of bananas in a pile, where 'm' represents the maximum
# number of bananas in any pile. For each potential eating speed within the
# binary search, the algorithm iterates through the 'n' piles of bananas to
# calculate the total time it takes Koko to eat all the bananas. This iteration
# to calculate the time takes O(n) time. Since binary search takes O(log m) and
# within each check we take O(n) to calculate the time, the overall time
# complexity is O(n log m).

# Space Complexity: O(1) – The algorithm predominantly uses a binary search
# approach which primarily involves arithmetic calculations and comparisons
# using a few variables to store the low, high and mid values of the search
# space. These variables take up constant space. There is no auxiliary data
# structure (like an array or hash map) that scales with the input size (number
# of piles of bananas). Therefore, the auxiliary space complexity is constant.