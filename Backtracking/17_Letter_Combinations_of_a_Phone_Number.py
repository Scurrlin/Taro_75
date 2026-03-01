class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        combos = ['']
        for d in digits:
            combos = [
                combo + letter
                for combo in combos
                for letter in digitMap[d]]
        return combos

# Time Complexity: O(4^n) – Let n be the length of the input digit string. Each
# digit maps to 3 or 4 letters. In the worst case, all digits map to 4 letters.
# The brute force approach explores every possible combination. For each digit,
# we potentially branch into 4 different possibilities. Thus, the number of
# possible combinations grows exponentially with the input size n. The total
# number of operations is approximately 4 * 4 * ... * 4 (n times) which is 4^n.
# Thus, the time complexity is O(4^n).

# Space Complexity: O(3^N) – The space complexity is dominated by the list used
# to store the letter combinations. In the worst-case scenario, where each digit
# maps to 3 letters (digits 2-6, 8), and the input has N digits, we can have up
# to 3^N combinations. We also use a temporary string to store current
# combination during recursion, which takes O(N) space, and the recursion stack
# can go up to depth N, which takes O(N) space. Since 3^N dominates N, the
# auxiliary space is O(3^N).