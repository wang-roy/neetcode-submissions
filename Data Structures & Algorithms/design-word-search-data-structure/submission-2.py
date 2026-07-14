class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        
        currentNode.isWord = True

    def search(self, word: str) -> bool:
        def dfs(word: str, node: TrieNode) -> bool:
            if word == "":
                return node.isWord
            
            char = word[0]
            if char == ".":
                for char in node.children:
                    result = dfs(word[1:], node.children[char])
                    if result == True:
                        return True
            elif char in node.children:
                return dfs(word[1:], node.children[char])

            return False
        return dfs(word, self.root)

        
