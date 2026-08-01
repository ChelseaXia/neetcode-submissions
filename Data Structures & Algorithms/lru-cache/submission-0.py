class Node: # 考虑使用双向链表，表头村最近最少使用的节点，表尾存最新访问的节点
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # 缓存总容量
        self.size = 0 #当前已经存了多少节点
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        # 初始化双向链表，加一个虚拟头尾
        self.head.next = self.tail
        self.tail.prev = self.head
    # 新增两个辅助函数，删除节点和把节点加到尾部
    def remove_node(self, node):
        # 把node从双向链表中移除
        node.prev.next = node.next
        node.next.prev = node.prev
    def add_to_tail(self, node):
        # 把某个节点加到尾部
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_tail(node)
            return node.value
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_tail(node)
            node.value = value
        else:
            node = Node(key=key, value=value)
            self.add_to_tail(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity: # 如果当前的缓存大小超过容量，要删除对应节点
                remove = self.head.next
                self.remove_node(remove)
                del self.cache[remove.key]
                self.size -= 1

        
