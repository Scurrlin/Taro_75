from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in counts.items():
            buckets[c].append(num)

        res = []
        for c in range(len(buckets) - 1, 0, -1):
            res.extend(buckets[c])
            if len(res) >= k:
                return res[:k]

# Time Complexity: O(n) – The first step involves counting the frequency of each
# element in the input array of size n, which takes O(n) time. The next step of
# organizing elements into buckets based on their frequency also takes O(n) time
# in the worst case, as each element could have a distinct frequency. Finally,
# iterating through the buckets to collect the top k elements is upper bounded
# by O(n) because in the worst case, we might need to examine all buckets.
# Therefore, the overall time complexity is dominated by the linear operations
# resulting in O(n).

# Space Complexity: O(N) – The algorithm uses a hash map to store the frequency
# of each element, which could potentially store all N elements of the input
# array. Additionally, it uses a list of lists (buckets) where the index
# represents the frequency and the value is a list of elements with that
# frequency. In the worst case, all elements are unique, leading to N buckets.
# Thus, the auxiliary space used is proportional to N, resulting in a space
# complexity of O(N).