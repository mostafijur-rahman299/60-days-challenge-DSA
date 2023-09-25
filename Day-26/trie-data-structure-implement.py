class Node:
    def __init__(self):
        self.children = [None]*26
        self.ew = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for letter in word:
            asci = ord(letter) - ord('a')
            if not root.children[asci]:
                root.children[asci] = Node()
            
            root = root.children[asci]
            
        root.ew = True

    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            asci = ord(letter) - ord('a')
            if not root.children[asci]:
                return False
            root = root.children[asci]
            
        if not root.ew: return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            asci = ord(letter) - ord('a')
            if not root.children[asci]:
                return False
            root = root.children[asci]
            
        return True
