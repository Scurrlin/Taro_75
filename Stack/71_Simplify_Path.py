class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split('/'):
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)

# Time Complexity: O(n) – The algorithm first splits the path string into a list
# of components based on the delimiter '/'. This operation takes O(n) time,
# where n is the length of the input path string. The algorithm then iterates
# through this list of components once. Inside the loop, operations like
# checking the component's value ('.', '..', or a directory name) and
# adding/removing elements to/from a stack or list take constant time, O(1).
# Since the loop iterates through all n components, the total time complexity of
# the loop is O(n). Finally, joining the elements from the stack with '/' takes
# O(m) time where m is the number of directories in the result, and in the worst
# case m will be proportional to n, so this operation can be considered O(n) as
# well. Therefore, the overall time complexity is dominated by the splitting and
# iteration steps, resulting in O(n).

# Space Complexity: O(N) – The solution uses a list to store the directory names
# of the simplified path. In the worst-case scenario, the input path contains N
# directory names that all need to be stored in this list. Therefore, the space
# required for the list grows linearly with the input size N, where N represents
# the number of components after splitting the initial path string.
# Consequently, the auxiliary space complexity is O(N).