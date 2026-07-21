class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] # 建一个先修课和当前课的图
        in_degree = [0] * numCourses # 计算所有课程的入度（表示有多少先修课）
        for course, pre in prerequisites:
            graph[pre].append(course) # 填充图
            in_degree[course] += 1 # 填充入度

        # 用BFS的方法去做
        # 先把不需要先修课的给上了
        courses = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        completed = 0 # 已上完的课
        while courses:
            cur = courses.popleft() 
            completed += 1
            for nextcourse in graph[cur]: # 把后续的课程都过一遍
                in_degree[nextcourse] -= 1
                if in_degree[nextcourse] == 0:
                    courses.append(nextcourse)
        if completed == numCourses:
            return True
        else:
            return False

