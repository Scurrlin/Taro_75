class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    visiting.remove(course)
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# Time Complexity: O(V + E) – We process each course (vertex) and each
# prerequisite (edge) once while building the graph and performing traversal.

# Space Complexity: O(V + E) – We store the graph (edges) and use additional
# space for visited tracking, recursion stack/queue, and output (vertices).