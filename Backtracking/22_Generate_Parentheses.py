class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        backtrack("", 0, 0)
        return res

# Time Complexity: O(4^n / (n * sqrt(n))) – The problem is solved using
# recursion (backtracking) where at each step, we have at most two choices:
# adding an opening parenthesis or a closing parenthesis. The depth of the
# recursion is 2n (since we add 2n parentheses in total). The number of valid
# parentheses combinations grows according to the Catalan numbers, which can be
# approximated by 4^n / (n * sqrt(n)). Each recursive call performs constant
# time operations (checks and appends). Therefore, the total time complexity is
# proportional to the number of valid combinations.

# Space Complexity: O(n) – The primary auxiliary space is consumed by the
# recursion stack. At any point, the depth of the recursion can go up to 2*n,
# representing the maximum length of a valid parenthesis string. Additionally, a
# list is used to store all generated valid parenthesis strings. If 'n'
# represents the number of pairs of parentheses, the number of valid
# combinations grows catalan(n), which is exponential. However, the space
# complexity for the recursion stack and the temporary string being built at any
# given recursion level is O(n). The final output storage is not typically
# counted as auxiliary space unless explicitly stated. Therefore, the dominant
# auxiliary space complexity is driven by the recursion depth and the temporary
# string construction, resulting in O(n).