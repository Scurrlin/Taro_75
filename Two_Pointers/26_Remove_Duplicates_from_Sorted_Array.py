class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# Time Complexity: O(n) – The time complexity is determined by the 'seeker'
# pointer, which must traverse the entire collection of numbers once to identify
# all unique elements. Let n be the number of elements in the input array. Since
# the seeker examines each of the n elements exactly one time, the total number
# of operations is directly proportional to n. The 'placement' pointer only
# moves when a unique element is found but does not add a separate loop or
# nested operations. Therefore, the complexity simplifies to a linear O(n).

# Space Complexity: O(1) – The algorithm operates in-place on the input
# collection and does not create any new data structures. The only extra memory
# used is for the two pointers, the 'placement' finger and the 'seeker' finger.
# The amount of memory required for these pointers is constant and does not
# scale with the size of the input collection, N. Therefore, the auxiliary space
# complexity is constant.