from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.listLen(head)
        k = k % l if l != 0 else 0
        if head is None or k == 0:
            return head
        current = head
        for _ in range(l - k - 1):
            current = current.next
            if current is None:
                return None
        last = current
        while last is not None and last.next is not None:
            last = last.next
        newStart = current.next
        current.next = None
        last.next = head
        return newStart

    def listLen(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        size = 0
        while head is not None:
            head = head.next
            size += 1
        return size


def arrToList(arr: list[int]) -> Optional[ListNode]:
    if len(arr) <= 0:
        return None
    current = result = ListNode(arr.pop(0))
    while len(arr) > 0:
        current.next = ListNode(arr.pop(0))
        current = current.next
    return result


def listToArr(lst: Optional[ListNode]) -> list[int]:
    result = []
    while lst is not None:
        result.append(lst.val)
        lst = lst.next
    return result
