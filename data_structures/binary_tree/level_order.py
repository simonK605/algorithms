"""
Level Order Traversal of Binary Tree (BFS)
-------------------------------------------
Traverse the binary tree level by level from left to right.

Time Complexity: O(n)
Space Complexity: O(n) – queue for BFS
"""

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


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

    print("Level order traversal:", level_order_traversal(root))
    # Output: [[1], [2, 3], [4, 5]]
