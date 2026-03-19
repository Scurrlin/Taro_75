class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)     
        return not stack

# Time Complexity: O(n) – The algorithm iterates through the input string once,
# examining each of the n characters. Inside the loop, the operations performed
# (checking if a character is an opening or closing parenthesis, matching
# parentheses, pushing/popping from the stack) take constant time, O(1).
# Therefore, the dominant factor is the single pass through the input string,
# resulting in a time complexity of O(n).

# Space Complexity: O(N) – The provided solution uses a stack to keep track of
# opening parentheses. In the worst-case scenario, the input string contains
# only opening parentheses (e.g., '((((((('), which would all be added to the
# stack. Thus, the stack can grow up to the size of the input string, N, where N
# is the length of the input string. Therefore, the auxiliary space complexity
# is O(N).