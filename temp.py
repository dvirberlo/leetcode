from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -inf

        def rec(v: Optional[TreeNode]) -> float:
            nonlocal result
            if v is None:
                return 0
            l, r = rec(v.left), rec(v.right)
            result = max(result, v.val, l + v.val, v.val + r, l + v.val + r)
            return max(v.val, l + v.val, v.val + r)

        rec(root)
        return int(result)

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        return int(self.B(root))

    def B(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return -inf
        if not hasattr(root, "B"):
            root.B = max(  # type: ignore
                root.val,
                self.B(root.left),
                self.B(root.right),
                self.O(root.left) + root.val,
                root.val + self.O(root.right),
                self.O(root.left) + root.val + self.O(root.right),
            )
        return root.B  # type: ignore

    def O(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return -inf
        if not hasattr(root, "O"):
            root.O = max(  # type: ignore
                root.val,
                self.O(root.left) + root.val,
                root.val + self.O(root.right),
            )
        return root.O  # type: ignore


def main():
    test([1, 4, 3, 2, 5, 2], 3)
    test([2, 1], 2)


def test(*args, **kwargs):
    r = Solution().maxPathSum(*args, **kwargs)
    print(r)


if __name__ == "__main__":
    main()
