"""
Doubly Linked List
-------------------
A doubly linked list allows traversal in both forward and backward directions.

Each node contains:
- data
- pointer to the next node
- pointer to the previous node

Supported operations:
- append (at end)
- prepend (at start)
- delete (by value)
- display forward and backward

Time Complexity:
- Append / Prepend: O(1)
- Delete: O(n)
- Display: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def prepend(self, data):
        """Add a node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        """Delete the first node with the given value."""
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # deleting head

                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    def display_forward(self):
        """Return values from head to tail."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            last = curr  # save tail for backward display
            curr = curr.next
        return result

    def display_backward(self):
        """Return values from tail to head."""
        result = []
        curr = self.head
        if not curr:
            return result

        # Go to the tail
        while curr.next:
            curr = curr.next

        # Traverse backward
        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(5)

    print("Forward:", dll.display_forward())   # [5, 10, 20, 30]
    print("Backward:", dll.display_backward()) # [30, 20, 10, 5]

    dll.delete(20)
    print("After deleting 20:")
    print("Forward:", dll.display_forward())   # [5, 10, 30]
