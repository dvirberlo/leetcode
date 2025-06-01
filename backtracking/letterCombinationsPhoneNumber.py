class Solution:
    options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    # options = [
    #     [],
    #     [],
    #     ["a", "b", "c"],
    #     ["d", "e", "f"],
    #     ["g", "h", "i"],
    #     ["j", "k", "l"],
    #     ["m", "n", "o"],
    #     ["p", "q", "r", "s"],
    #     ["t", "u", "v"],
    #     ["w", "x", "y", "z"],
    # ]

    # def options(self, d: int) -> list[str]:
    #     match d:
    #         case 2:
    #             return ["a", "b", "c"]
    #         case 3:
    #             return ["d", "e", "f"]
    #         case 4:
    #             return ["g", "h", "i"]
    #         case 5:
    #             return ["j", "k", "l"]
    #         case 6:
    #             return ["m", "n", "o"]
    #         case 7:
    #             return ["p", "q", "r", "s"]
    #         case 8:
    #             return ["t", "u", "v"]
    #         case 9:
    #             return ["w", "x", "y", "z"]
    #     return []

    # def options(self, d: int) -> str:
    #     match d:
    #         case 2:
    #             return "abc"
    #         case 3:
    #             return "def"
    #         case 4:
    #             return "ghi"
    #         case 5:
    #             return "jkl"
    #         case 6:
    #             return "mno"
    #         case 7:
    #             return "pqrs"
    #         case 8:
    #             return "tuv"
    #         case 9:
    #             return "wxyz"
    #     return ""

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        last = [""]
        for c in digits:
            current = []
            for l in self.options[int(c)]:
                current.extend(w + l for w in last)
            last = current
        return last