class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

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
