class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((curr, num))
                curr = ""
                num = 0
            elif char == ']':
                prev, repeat = stack.pop()
                curr = prev + repeat * curr
            else:
                curr += char
        return curr

# Time Complexity: O(n*m) – The algorithm iterates through the input string of
# length n once. Inside the loop, when a closing bracket ']' is encountered, the
# string preceding the bracket needs to be constructed by popping elements from
# the stack, which, in the worst case, may involve concatenating a substring
# with a length proportional to the repetition count m times, where m is the
# count to repeat a string. Therefore, the complexity depends on both n (the
# length of the input string) and m (the number of repetitions which can be
# variable dependent on the input). The most computationally expensive part is
# constructing the repeated substring, leading to O(n*m) complexity in the
# worst-case scenario where the decoded string is much larger than the input due
# to high repetition counts. Hence the overall time complexity is O(n*m).

# Space Complexity: O(S) – where S is the length of the fully decoded output
# string. The stack stores partially decoded strings and repetition counts. With
# nested patterns like 'k[k[...]]', the intermediate strings held on the stack
# and in curr can grow far beyond the input length (e.g., '1000[abc]' has input
# length ~9 but decoded length 3000). The dominant space cost is therefore
# proportional to the decoded output size, not the input size.