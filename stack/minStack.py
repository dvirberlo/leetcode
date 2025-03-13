class MinStack:
    def __init__(self):
        self.minVals = []
        self.vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        self.minVals.append(min(val, self.minVals[-1] if self.minVals else val))

    def pop(self) -> None:
        self.minVals.pop()
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
