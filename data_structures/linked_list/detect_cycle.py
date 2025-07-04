"""
Detect Cycle in a Singly Linked List
-------------------------------------
This implementation uses Floyd's Cycle Detection Algorithm (Tortoise and Hare).

If a loop exists in the linked list, the slow and fast pointers will eventually meet.

Time Complexity: O(n)
Space Complexity: O(1) – constant space
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move by 1 step
        fast = fast.next.next     # move by 2 steps

        if slow == fast:
            return True           # cycle detected

    return False                  # no cycle


if __name__ == "__main__":
    # Create nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    # Create linked list: 1 -> 2 -> 3 -> 4
    a.next = b
    b.next = c
    c.next = d

    # Case 1: No cycle
    print("Has cycle?", has_cycle(a))  # Output: False

    # Case 2: Create a cycle: 4 → 2
    d.next = b
    print("Has cycle?", has_cycle(a))  # Output: True
