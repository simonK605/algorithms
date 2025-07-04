"""
Binary Tree Implementation
---------------------------
Basic structure for a binary tree with:
- Insert (manual construction)
- Inorder Traversal (Left, Root, Right)
- Preorder Traversal (Root, Left, Right)
- Postorder Traversal (Left, Right, Root)

Time Complexity:
- Insert (manual): O(1)
- Traversals: O(n)
Space Complexity: O(n) for recursion stack in traversals
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)


if __name__ == "__main__":
    # Create a sample binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    bt = BinaryTree(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)

    # Inorder Traversal
    inorder = []
    bt.inorder_traversal(bt.root, inorder)
    print("Inorder Traversal:", inorder)  # Output: [4, 2, 5, 1, 3]

    # Preorder Traversal
    preorder = []
    bt.preorder_traversal(bt.root, preorder)
    print("Preorder Traversal:", preorder)  # Output: [1, 2, 4, 5, 3]

    # Postorder Traversal
    postorder = []
    bt.postorder_traversal(bt.root, postorder)
    print("Postorder Traversal:", postorder)  # Output: [4, 5, 2, 3, 1]
