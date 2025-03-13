function copyRandomList1(
  head: _Node | null,
  map: Map<_Node, _Node> = new Map()
): _Node | null {
  if (head == null) return head;
  if (map.has(head)) return map.get(head)!;
  const node = new _Node(head.val);
  map.set(node, node);
  map.set(head, node);
  const next = copyRandomList1(head.next, map);
  const random = copyRandomList1(head.random, map);
  node.next = next;
  node.random = random;
  return node;
}
function copyRandomList2(head: _Node | null): _Node | null {
  if (head == null) return head;
  const map = new Map<_Node, _Node>();
  const result = new _Node(head.val, undefined, head.random!);
  map.set(head, result);
  let last = result,
    current = head.next;
  while (current != null) {
    const node = new _Node(current.val, undefined, current.random!);
    last.next = node;
    map.set(current, node);
    last = last.next;
    current = current.next;
  }
  current = result;
  while (current != null) {
    if (current.random != null) current.random = map.get(current.random)!;
    current = current.next;
  }
  return result;
}
function copyRandomList(head: _Node | null): _Node | null {
  if (head == null) return head;
  let current: _Node | null = head,
    next;
  while (current != null) {
    next = current.next;
    const copy: _Node = new _Node(current.val);
    current.next = copy;
    current = copy.next = next;
  }
  current = head;
  while (current != null) {
    if (current.random != null) current.next!.random = current.random.next;
    current = current.next!.next;
  }
  const result = head!.next;
  current = head;
  while (current != null) {
    next = current.next!.next;

    current.next!.next = next?.next ?? null;

    current.next = next;
    current = next;
  }
  return result;
}
