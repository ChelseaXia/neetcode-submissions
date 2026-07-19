class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index): # node代表读到哪一个房间，index代表搜索到当前的第几个字符
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                if c =='.': # 通配符处理方法
                    for child in cur.children.values(): # 需要遍历所有孩子
                        if dfs(child, i+1): # 和下一个字符匹配，只要有一个找到了
                            return True
                    return False
                else: # 正常字符走这一条
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(self.root, 0)


        
