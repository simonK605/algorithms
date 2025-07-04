"""
Reverse a Singly Linked List
------------------------------
This script reverses a singly linked list in-place.

Time Complexity: O(n)
Space Complexity: O(1) – no extra space used
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next   # store next
            curr.next = prev        # reverse current node's pointer
            prev = curr             # move prev and curr one step forward
            curr = next_node

        self.head = prev

    def display(self):
        """Return list elements as Python list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Original List:     ", ll.display())  # [1, 2, 3, 4]

    ll.reverse()

    print("Reversed List:     ", ll.display())  # [4, 3, 2, 1]
