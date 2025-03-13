import collections
from math import inf
from typing import Optional


class Vertex:
    def __init__(self, key: int, value=None) -> None:
        self.key = key
        self.value = value
        self.neighbors: set[int] = set()

    def __str__(self):
        return f"{self.key}, {self.value}, {self.neighbors}"


class Graph:
    def __init__(self, size=0) -> None:
        self.vertices = [Vertex(i) for i in range(size)]

    def addVertex(self, value=None):
        v = Vertex(len(self.vertices), value)
        self.vertices.append(v)
        return v.key

    def getVertex(self, key: int):
        return self.vertices[key] if 0 <= key < len(self.vertices) else None

    def addEdge(self, src: int, dst: int):
        self.vertices[src].neighbors.add(dst)

    def addSimpleEdge(self, v: int, u: int):
        self.addEdge(u, v)
        self.addEdge(v, u)

    def distance(self, src: int, dst: int):
        # return 0
        d = [inf for _ in range(len(self.vertices))]
        c = [False for _ in range(len(self.vertices))]
        q = [src]
        d[src] = 0
        while q:
            v = q.pop(0)
            c[v] = True
            for u in self.vertices[v].neighbors:
                if not c[u]:
                    q.append(u)
                d[u] = min(d[u], d[v] + 1)
        return d[dst]

    def __str__(self):
        return "\n".join(str(v) for v in self.vertices)


class Solution:
    def ladderLength1(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        e = 0
        try:
            e = wordList.index(endWord)
        except ValueError:
            return 0

        n = len(wordList)
        g = Graph()
        for i in range(n):
            g.addVertex(wordList[i])
        s = g.addVertex(beginWord)
        for i in range(n):
            if self.oneHammingDistance(beginWord, wordList[i]):
                g.addSimpleEdge(s, i)
            for j in range(i + 1, n):
                if self.oneHammingDistance(wordList[i], wordList[j]):
                    g.addSimpleEdge(i, j)
        d = g.distance(s, e)
        return 0 if d == inf else int(d + 1)

    def ladderLength2(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        e = 0
        try:
            e = wordList.index(endWord)
        except ValueError:
            return 0

        n = len(wordList)
        g = Graph(n)
        s = g.addVertex()
        for i in range(n):
            if self.oneHammingDistance(beginWord, wordList[i]):
                g.addSimpleEdge(s, i)
            if self.oneHammingDistance(endWord, wordList[i]):
                g.addSimpleEdge(e, i)
            for j in range(i + 1, n):
                if self.oneHammingDistance(wordList[i], wordList[j]):
                    g.addSimpleEdge(i, j)
        d = g.distance(s, e)
        return 0 if d == inf else int(d + 1)

    def ladderLength3(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        e = 0
        try:
            e = wordList.index(endWord)
        except ValueError:
            return 0

        n = len(wordList)
        g = Graph(n + 1)
        wordList.append(beginWord)
        s = n
        m = len(beginWord)
        for i in range(n):
            w = wordList[i]
            for t in range(m):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    try:
                        j = wordList.index(w[:t] + c + w[t + 1 :])
                        g.addEdge(i, j)
                    except ValueError:
                        continue
        d = g.distance(s, e)
        return 0 if d == inf else int(d + 1)

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        m = len(beginWord)
        q = [(beginWord, 1)]
        while q:
            w, d = q.pop(0)
            if w == endWord:
                return d
            for i in range(m):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    t = w[:i] + c + w[i + 1 :]
                    if t in words:
                        words.remove(t)
                        q.append((t, d + 1))
        return 0

    def oneHammingDistance(self, w1: str, w2: str) -> bool:
        return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1
