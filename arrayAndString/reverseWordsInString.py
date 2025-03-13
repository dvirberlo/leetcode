class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            word = ""
            while i < n and s[i] != " ":
                word += s[i]
                i += 1
            if word != "":
                words.append(word)
        print(words)
        return " ".join(reversed(words))
