class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for n in nums:
            l, r = 0, len(tails)

            while l < r:
                mid = (l + r)//2
                if tails[mid] < n:
                    l = mid + 1
                else:
                    r = mid

  
            if l == len(tails):
                tails.append(n)
            else:
                tails[l] = n

        return len(tails)

# Time Complexity: O(n log n) – We iterate through the input sequence of size n.
# For each element, we perform a binary search on a sorted list of the smallest
# tail elements of increasing subsequences. The binary search takes O(log n)
# time. Since we perform this binary search for each of the n elements, the
# overall time complexity is O(n log n).

# Space Complexity: O(N) – The algorithm maintains a list of the last elements
# of increasing subsequences. In the worst case, the input sequence is already
# increasing, and this list will store all N elements of the input sequence.
# Therefore, the auxiliary space used scales linearly with the size of the input
# sequence. This results in a space complexity of O(N).