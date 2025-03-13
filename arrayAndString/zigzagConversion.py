class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows: list[str] = [""] * numRows
        i = 0
        step = 1
        for l in s:
            rows[i] += l
            if i == 0:
                step = 1
            if i == numRows - 1:
                step = -1
            i += step
        return "".join(rows)
