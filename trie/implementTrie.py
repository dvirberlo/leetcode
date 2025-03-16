from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.value = 0
        self.children: defaultdict[str, TrieNode] = defaultdict(TrieNode)


class Trie1:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            current.value = max(1, current.value)
            current = current.children[c]
        current.value = max(2, current.value)

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.value == 2

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.value >= 1


class Trie:
    def __init__(self):
        self.root: dict[str, dict] = dict()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = dict()
            current = current[c]
        current[""] = None  # type: ignore

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return "" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True
