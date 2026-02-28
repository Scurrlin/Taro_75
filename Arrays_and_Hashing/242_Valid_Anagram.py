class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        count = {}
        for a, b in zip(s, t):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1
        return all(val == 0 for val in count.values())

# Time Complexity: O(n) – The algorithm makes a single pass through both strings using zip, processing n character pairs. Each iteration performs constant-time dictionary operations (insertion/update), which are O(1) on average. The final check using all(...) iterates over the dictionary values, which in the worst case is bounded by the number of distinct characters (at most n, or constant if the alphabet is fixed). Therefore, the overall time complexity is O(n).

# Space Complexity: O(1) – The solution uses a dictionary to store character counts. In the worst case, the dictionary holds at most k distinct characters, where k is the size of the character set. For lowercase English letters, k ≤ 26, which is constant. Therefore, the auxiliary space complexity is O(1).