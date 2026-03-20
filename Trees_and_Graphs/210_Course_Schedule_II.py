class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for course, p in prerequisites:
            preMap[course].append(p)
        visit, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for p in preMap[course]:
                if dfs(p) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

# Time Complexity: O(V + E) – We process each course (vertex) and each
# prerequisite (edge) once while building the graph and performing traversal.

# Space Complexity: O(V + E) – We store the graph (edges) and use additional
# space for visited tracking, recursion stack/queue, and output (vertices).