class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Time Complexity: O(n) – The initial step of adding all numbers to a set takes
# O(n) time. The main loop iterates through each of the n numbers in the input.
# Inside the loop, the 'if' condition checks for the existence of the previous
# number in the set, which is O(1). The 'while' loop, which extends the
# consecutive sequence, on average, will not run for every number. This is
# because it only runs when a number is the potential start of a sequence. Each
# number within the input can only be part of one consecutive sequence.
# Therefore, the total number of times the 'while' loop iterates across all
# numbers remains bounded by n. Therefore, the overall time complexity
# approximates O(n).

# Space Complexity: O(N) – The solution uses a set to store all the numbers from
# the input array. This set requires space proportional to the number of
# elements in the input, where N is the number of integers in the input array.
# Therefore, the auxiliary space used is directly dependent on the size of the
# input. No other significant auxiliary space is used beyond this set, leading
# to a space complexity of O(N).