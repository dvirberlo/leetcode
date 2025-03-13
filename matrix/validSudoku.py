class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        numbers = set()
        # rows
        for i in range(n):
            numbers.clear()
            for j in range(n):
                current = board[i][j]
                if current != "." and current in numbers:
                    return False
                numbers.add(current)
        # columns
        for j in range(n):
            numbers.clear()
            for i in range(n):
                current = board[i][j]
                if current != "." and current in numbers:
                    return False
                numbers.add(current)
        # cubes:
        for i in range(n):
            numbers.clear()
            for j in range(n):
                current = board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]
                if current != "." and current in numbers:
                    return False
                numbers.add(current)
        return True
