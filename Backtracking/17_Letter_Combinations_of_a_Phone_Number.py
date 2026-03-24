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

# Time Complexity: O(n * 4^n) – Let n be the length of the input digit string.
# In the worst case every digit maps to 4 letters (digits 7 and 9), producing
# up to 4^n combinations. The algorithm builds these iteratively: for each
# digit, it creates new strings by concatenating every existing combo with every
# letter for that digit. Each string concatenation produces a new string of
# length up to n, so the total work is O(n * 4^n).

# Space Complexity: O(n * 4^n) – The algorithm is purely iterative (no recursion
# stack). Space is dominated by the combos list, which holds up to 4^n strings
# each of length n. Therefore, the total space for the output is O(n * 4^n).