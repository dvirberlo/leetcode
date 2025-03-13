from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        current = dummy = ListNode(-1, head)
        l = self.listLen(head)

        for _ in range(l // k):
            if current is None:
                break
            next = current.next
            self.reverseLen(current, k - 1)
            current = next
        return dummy.next

    def listLen(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        size = 0
        while head is not None:
            head = head.next
            size += 1
        return size

    def reverseLen(self, prev: ListNode, count: int) -> Optional[ListNode]:
        if count < 1 or prev.next is None or prev.next.next is None:
            return prev.next.next if prev.next is not None else None
        last = prev
        current = prev.next
        next = prev.next.next
        for _ in range(count):
            last = current
            current = next
            next = current.next
            current.next = last
            last = current
            if next is None:
                break
        prev.next.next = next
        prev.next = current
        return next


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
