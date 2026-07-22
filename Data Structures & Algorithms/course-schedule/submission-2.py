class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]:
            return True
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        courses = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while courses:
            cur = courses.popleft()
            for next in graph[cur]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    courses.append(next)
            count += 1
        return count == numCourses