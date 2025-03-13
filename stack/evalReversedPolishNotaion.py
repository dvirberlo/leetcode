class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s: list[int] = []
        for t in tokens:
            match t:
                case "+":
                    b, a = s.pop(), s.pop()
                    s.append(a + b)
                case "-":
                    b, a = s.pop(), s.pop()
                    s.append(a - b)
                case "*":
                    b, a = s.pop(), s.pop()
                    s.append(a * b)
                case "/":
                    b, a = s.pop(), s.pop()
                    s.append(int(a / b))
                case _:
                    s.append(int(t))
        return s.pop()
