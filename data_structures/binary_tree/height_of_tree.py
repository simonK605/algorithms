"""
Height of Binary Tree
----------------------
The height (or depth) of a binary tree is the number of nodes
on the longest path from the root to a leaf.

Time Complexity: O(n)
Space Complexity: O(n) — for recursion stack in worst case (skewed tree)
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def height_of_tree(node):
    if node is None:
        return 0
    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)
    return 1 + max(left_height, right_height)


if __name__ == "__main__":
    # Example tree:
    #        1
    #       / \
    #      2   3
    #     /
    #    4

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("Height of tree:", height_of_tree(root))  # Output: 3
