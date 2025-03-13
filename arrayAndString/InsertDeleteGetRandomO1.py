import random


class RandomizedSet:

    def __init__(self):
        self.list: list[int] = list()
        self.dict: dict[int, int] = dict()

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        idx = self.dict[val]
        replacement = self.list[-1]
        self.list[idx] = replacement
        self.dict[replacement] = idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
