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

# Time Complexity: O(1) – The approach uses two stacks, one for the actual data
# and one to track the minimum element at each step. When pushing an element, we
# push the new element onto the data stack and the minimum of the new element
# and the current minimum onto the min-tracking stack. When popping, we pop from
# both stacks. When getting the minimum, we simply peek at the top of the
# min-tracking stack. All these operations involve a constant number of stack
# operations, regardless of the number of elements (n) currently in the stack.
# Therefore, each operation takes constant time.

# Space Complexity: O(n) – The solution uses two storage areas: one for the main
# numbers and another to track the minimum at each step. Both of these storage
# areas will store an entry for each element pushed onto the stack. If 'n' is
# the number of elements in the stack, the auxiliary space required by these two
# storage areas grows linearly with 'n'. Therefore, the space complexity is
# O(n).