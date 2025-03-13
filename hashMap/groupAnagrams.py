from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in strs:
            groups[self.hash(w)].append(w)
        return list(groups.values())

    def hash(self, s: str):
        # return "".join(sorted(s))
        result = [0] * 26
        for l in s:
            result[ord(l) - ord("a")] += 1
        return ",".join(str(e) for e in result)

    def lowercase_letters(self):
        for letter in range(ord("a"), ord("z") + 1):
            yield chr(letter)

    def getLetters(self, s: str) -> defaultdict:
        letters = defaultdict(int)
        for l in s:
            letters[l] += 1
        return letters

    def isAnagram(self, s: str, t: str) -> bool:
        print(list(self.getLetters(s).keys()), list(self.getLetters(t).keys()))
        return self.getLetters(s) == self.getLetters(t)
