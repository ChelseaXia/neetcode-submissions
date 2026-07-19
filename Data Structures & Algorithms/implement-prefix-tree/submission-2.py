class TrieNode: # 定义前缀树结构
    def __init__(self):
        self.children = {} # 哈希做法
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        # 这里要写根节点
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c] # 这里要基于当前值继续寻找下一个
        if cur.endOfWord: # 需要验证是不是末尾
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        