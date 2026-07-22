class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs解法
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        visited = [0]*numCourses
        def dfs(i):
            if visited[i]==1: return False # 如果正在上这节课，但是又是下一节课的先修课，就形成了环
            if visited[i]==2: return True # 如果已经上完了，就可以正常上课
            visited[i] = 1
            for next in graph[i]:
                if not dfs(next): return False
            visited[i] = 2 # 修改安全标记
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True