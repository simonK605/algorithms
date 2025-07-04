"""
Check if Binary Tree is Height-Balanced
----------------------------------------
A binary tree is balanced if for every node:
  |height(left subtree) - height(right subtree)| <= 1

Time Complexity: O(n)
  - We calculate height while checking balance in one pass.
Space Complexity: O(n) for recursion stack
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def is_balanced(root):
    def check(node):
        if not node:
            return 0  # Height is 0

        left = check(node.left)
        if left == -1:
            return -1

        right = check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1  # Not balanced

        return 1 + max(left, right)

    return check(root) != -1


if __name__ == "__main__":
    # Balanced binary tree
    #       1
    #      / \
    #     2   3
    #    /
    #   4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("Is tree balanced?", is_balanced(root))  # Output: True

    # Unbalanced binary tree
    #       1
    #      /
    #     2
    #    /
    #   3

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)

    print("Is tree balanced?", is_balanced(root2))  # Output: False
