class TrieNode: # 定义前缀树结构
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        # 这里要写根节点
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i] # 这里要基于当前值继续寻找下一个
        if cur.endOfWord: # 需要验证是不是末尾
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c)-ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True
        
        