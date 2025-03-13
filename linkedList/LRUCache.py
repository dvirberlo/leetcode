from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, prev=None, next=None, key=0):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, ListNode] = dict()

        self.lru = ListNode(-1, None, None)
        self.mru = ListNode(-2, None, None)
        self.mru.prev = self.lru
        self.lru.next = self.mru

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]

        node.prev.next = node.next  # type: ignore
        node.next.prev = node.prev  # type: ignore

        self.mru.prev.next = node  # type: ignore
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map and len(self.map) >= self.capacity:
            deleted = self.lru.next
            self.lru.next = deleted.next  # type: ignore
            deleted.next.prev = self.lru  # type: ignore
            del self.map[deleted.key]  # type: ignore

        if key in self.map:
            node = self.map[key]
            node.val = value
            node.prev.next = node.next  # type: ignore
            node.next.prev = node.prev  # type: ignore
        else:
            self.map[key] = ListNode(value, key=key)
        node = self.map[key]

        self.mru.prev.next = node  # type: ignore
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
