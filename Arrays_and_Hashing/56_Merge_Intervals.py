class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

# Time Complexity: O(n log n) – The initial step involves sorting the input
# intervals based on their start times, which takes O(n log n) time.
# Subsequently, we iterate through the sorted intervals once, performing
# constant-time comparisons and merges. This linear pass contributes O(n) time.
# Since sorting dominates the time complexity, the overall time complexity is
# O(n log n) + O(n), which simplifies to O(n log n).

# Space Complexity: O(n) – The primary auxiliary space used is for storing the
# 'merged' intervals. In the worst case, where no intervals overlap, we will
# store all N input intervals in a new list. This list will grow proportionally
# to the number of intervals in the input. Therefore, the auxiliary space
# complexity is O(n), where n is the number of intervals in the input.