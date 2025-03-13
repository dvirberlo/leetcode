class Solution:

    letters: dict[int, str] = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def intToRoman(self, num: int) -> str:
        result_list: list[str] = []
        for v, l in Solution.letters.items():
            while num >= v:
                result_list.append(l)
                num -= v
        return "".join(result_list)
