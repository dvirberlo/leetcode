class WordDictionary:
    def __init__(self):
        self.root: dict[str, dict] = dict()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = dict()
            current = current[c]
        current[""] = None  # type: ignore

    def search(self, word: str, current=None) -> bool:
        current = self.root if current is None else current
        for i, c in enumerate(word):
            if c == ".":
                for e in current.values():
                    if e is not None and self.search(word[i + 1 :], e):
                        return True
                return False
            elif c not in current:
                return False
            current = current[c]
        return "" in current
