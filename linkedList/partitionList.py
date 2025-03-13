from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        lastLess = dummyLess = ListNode()
        lastGreater = dummyGreater = ListNode()
        current = head
        while current is not None:
            next = current.next
            if current.val < x:
                lastLess.next = current
                lastLess = lastLess.next
                lastLess.next = None
            else:
                lastGreater.next = current
                lastGreater = lastGreater.next
                lastGreater.next = None
            current = next
        lastLess.next = dummyGreater.next
        return dummyLess.next


def arrToList(arr: list[int]) -> Optional[ListNode]:
    if len(arr) <= 0:
        return None
    current = result = ListNode(arr.pop(0))
    while len(arr) > 0:
        current.next = ListNode(arr.pop(0))
        current = current.next
    return result