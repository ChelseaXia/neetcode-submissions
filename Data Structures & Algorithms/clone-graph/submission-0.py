"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        visited[node] = Node(node.val)
        q = deque([node]) # 这里记得要把node加一个中括号，but why？
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor) # 把新的邻居加到队列里准备处理
                visited[cur].neighbors.append(visited[neighbor])
        return visited[node]
                    
                