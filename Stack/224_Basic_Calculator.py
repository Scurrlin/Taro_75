class Solution:
    def calculate(self, s: str) -> int:
        res, n = 0, 0
        stack, sign = [], 1

        for char in s:
            if char.isdigit():
                n = n * 10 + int(char)

            elif char == '+':
                res += sign * n
                n, sign = 0, 1

            elif char == '-':
                res += sign * n
                n, sign = 0, -1

            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1

            elif char == ')':
                res += sign * n
                n = 0

                res *= stack.pop()
                res += stack.pop()

        return res + sign * n

# Time Complexity: O(n) – The algorithm makes a single pass through the input
# string of length n. Each character is processed exactly once with constant-time
# work: digit characters are accumulated into the current number, operators
# update the running result, and parentheses push/pop the stack in O(1). The
# total work is therefore proportional to n.

# Space Complexity: O(n) – A stack is used to save the accumulated result and
# sign whenever an opening parenthesis is encountered. In the worst case (deeply
# nested expressions), the stack depth can grow proportionally to n. Therefore,
# the auxiliary space is O(n).