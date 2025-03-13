from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current = dummy = ListNode(0, head)
        while current is not None and current.next is not None:
            x = current.next.val
            preLast = current
            while current.next is not None and current.next.val == x:
                current = current.next
            if preLast.next is not current:
                preLast.next = current.next
                current = preLast
        return dummy.next


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
