// Definition for singly-linked list.
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  let c1: ListNode | undefined | null = l1,
    c2: ListNode | undefined | null = l2,
    c: ListNode | null = null,
    result: ListNode | null = null,
    carry = 0;
  while (carry > 0 || c1 != null || c2 != null) {
    carry += (c1?.val ?? 0) + (c2?.val ?? 0);
    if (c != null) {
      c.next = new ListNode(carry % 10);
      c = c.next;
    } else result = c = new ListNode(carry % 10);
    carry = Math.floor(carry / 10);
    c1 = c1?.next;
    c2 = c2?.next;
  }
  return result;
}

function arrayToList(arr: number[]): ListNode | null {
  let result: ListNode | null = null;
  while (arr.length) result = new ListNode(arr.pop(), result);
  return result;
}

function listToArray(list: ListNode | null): number[] {
  const result: number[] = [];
  while (list != null) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}
