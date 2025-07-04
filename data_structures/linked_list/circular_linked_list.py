"""
Circular Linked List
---------------------
In a circular linked list, the last node points back to the head.

Supports:
- Append
- Display
- Delete node by value

Time Complexity:
- Append: O(n)
- Delete: O(n)
- Display: O(n)

Space Complexity: O(n) total for n nodes
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def display(self):
        nodes = []
        if not self.head:
            return nodes

        curr = self.head
        while True:
            nodes.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        return nodes

    def delete(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        # Special case: deleting head node
        while True:
            if curr.data == key:
                if prev is None:  # Head node
                    # Find last node
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:
                        self.head = None  # Only one node
                    else:
                        self.head = self.head.next
                        tail.next = self.head
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.append(40)

    print("Circular Linked List:")
    print(cll.display())  # Output: [10, 20, 30, 40]

    cll.delete(30)
    print("After deleting 30:")
    print(cll.display())  # Output: [10, 20, 40]

    cll.delete(10)
    print("After deleting 10 (head):")
    print(cll.display())  # Output: [20, 40]
