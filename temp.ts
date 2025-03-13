class _Node {
  val: number;
  next: _Node | null;
  random: _Node | null;

  constructor(val?: number, next?: _Node, random?: _Node) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}

function arrayToList(arr: number[]): _Node | undefined {
  let result: _Node | undefined;
  while (arr.length) result = new _Node(arr.pop(), result);
  return result;
}

function listToArray(list: _Node | null): number[] {
  const result: number[] = [];
  while (list != null) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}

function test(l: number[]) {
  console.log();
}

function main() {
  test([1, 2, 4]);
  test([], []);
  test([], [0]);
}

main();
