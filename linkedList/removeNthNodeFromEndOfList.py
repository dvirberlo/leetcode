from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        current = prevN = dummy = ListNode(-1, head)
        for _ in range(n + 1):
            if current is None:
                return head
            current = current.next
        while current is not None:
            current = current.next
            prevN = prevN.next  # type: ignore
        prevN.next = prevN.next.next  # type: ignore
        return dummy.next

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        l = self.listLen(head)
        current = dummy = ListNode(-1, head)
        for _ in range(l - n):
            if current is None:
                return head
            current = current.next
        if current is None or current.next is None:
            return head
        current.next = current.next.next
        return dummy.next

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
