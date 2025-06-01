from typing import Optional


# class Trie:
#     found = ""

#     def __init__(self):
#         self.root: dict[str, dict] = dict()

#     def insert(self, word: str) -> None:
#         current = self.root
#         for c in word:
#             if c not in current:
#                 current[c] = dict()
#             current = current[c]
#         current[Trie.found] = None  # type: ignore

#     def remove(self, word: str) -> None:
#         current = self.root
#         alone = None
#         for c in word:
#             if c not in current:
#                 return
#             elif len(current[c]) > 1:
#                 alone = None
#             else:
#                 alone = current if alone is None else alone
#             current = current[c]
#         if Trie.found not in current:
#             return
#         del current[Trie.found]
#         current = self.root
#         for c in word:
#             if c not in current:
#                 return
#             elif alone is current:
#                 alone = current[c]
#                 del current[c]
#                 current = alone
#             else:
#                 current = current[c]

#     def get(self, word: str) -> Optional[dict[str, dict]]:
#         current = self.root
#         for c in word:
#             if c not in current:
#                 return None
#             current = current[c]
#         return current

#     def search(self, word: str) -> bool:
#         current = self.root
#         for c in word:
#             if c not in current:
#                 return False
#             current = current[c]
#         return Trie.found in current

#     def startsWith(self, prefix: str) -> bool:
#         current = self.root
#         for c in prefix:
#             if c not in current:
#                 return False
#             current = current[c]
#         return True


# class Solution:

#     def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
#         result = list()
#         t = Trie()
#         for w in words:
#             t.insert(w)
#         n, m = len(board), len(board[0])
#         visited = "*"

#         def b(i, j) -> Optional[str]:
#             nonlocal board
#             return board[i][j] if (0 <= i < n and 0 <= j < m) else None

#         def search(i, j, w=""):
#             if not (0 <= i < n and 0 <= j < m) or board[i][j] == visited:
#                 return
#             nonlocal t
#             l = board[i][j]
#             w = w + l
#             d = t.get(w)
#             if d is None:
#                 return
#             if Trie.found in d:
#                 result.append(w)
#                 t.remove(w)
#             board[i][j] = visited
#             search(i - 1, j, w)
#             search(i, j - 1, w)
#             search(i + 1, j, w)
#             search(i, j + 1, w)
#             board[i][j] = l

#         for i in range(n):
#             for j in range(m):
#                 search(i, j)
#         return result


class Trie:
    found = ""

    def __init__(self):
        self.root: dict[str, dict] = dict()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current[c] = dict()
            current = current[c]
        current[Trie.found] = None  # type: ignore

    def remove(self, word: str) -> None:
        current = self.root
        alone = None
        for c in word:
            if c not in current:
                return
            elif len(current[c]) > 1:
                alone = None
            else:
                alone = current if alone is None else alone
            current = current[c]
        if Trie.found not in current:
            return
        del current[Trie.found]
        current = self.root
        for c in word:
            if c not in current:
                return
            elif alone is current:
                alone = current[c]
                del current[c]
                current = alone
            else:
                current = current[c]


class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        result = list()
        t = Trie()
        for w in words:
            t.insert(w)
        n, m = len(board), len(board[0])
        visited = "*"

        def search(i, j, w="", node: dict[str, dict] = t.root):
            if not (0 <= i < n and 0 <= j < m) or board[i][j] == visited:
                return
            nonlocal t
            l = board[i][j]
            w = w + l
            if l not in node:
                return
            node = node[l]
            if Trie.found in node:
                result.append(w)
                t.remove(w)
            board[i][j] = visited
            search(i - 1, j, w, node)
            search(i, j - 1, w, node)
            search(i + 1, j, w, node)
            search(i, j + 1, w, node)
            board[i][j] = l

        for i in range(n):
            for j in range(m):
                search(i, j)
        return result
