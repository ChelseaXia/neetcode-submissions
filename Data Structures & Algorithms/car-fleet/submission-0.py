class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for p, s in cars:
            stack.append((target-p)/s) # 从大到小将到达用时压进栈
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # 如果前面的用时小于等于后面，合并
        return len(stack)


