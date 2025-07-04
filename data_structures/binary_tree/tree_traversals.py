"""
Binary Tree Traversals
-----------------------
This file includes:
- Inorder Traversal (Left, Root, Right)
- Preorder Traversal (Root, Left, Right)
- Postorder Traversal (Left, Right, Root)

Time Complexity: O(n) for all traversals
Space Complexity: O(n) for recursion stack in worst case
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.val)
        inorder_traversal(node.right, result)


def preorder_traversal(node, result):
    if node:
        result.append(node.val)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)


def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.val)


if __name__ == "__main__":
    # Example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    inorder = []
    preorder = []
    postorder = []

    inorder_traversal(root, inorder)
    preorder_traversal(root, preorder)
    postorder_traversal(root, postorder)

    print("Inorder Traversal:  ", inorder)     # [4, 2, 5, 1, 3]
    print("Preorder Traversal: ", preorder)    # [1, 2, 4, 5, 3]
    print("Postorder Traversal:", postorder)   # [4, 5, 2, 3, 1]
