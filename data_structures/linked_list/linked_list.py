"""
Singly Linked List
--------------------
A linear data structure where each element points to the next.

Supports:
- Append
- Prepend
- Delete by value
- Search
- Display

Time Complexity:
- Append / Prepend: O(1) or O(n) depending on tail pointer
- Delete / Search: O(n)
- Display: O(n)

Space Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        """Add node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete first node with the given value"""
        curr = self.head
        prev = None

        while curr:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next  # deleting head
                return
            prev = curr
            curr = curr.next

    def search(self, key):
        """Search for a value and return True if found"""
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def display(self):
        """Return list elements as a Python list"""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)

    print("Linked List:", ll.display())         # [5, 10, 20]
    print("Search 10:", ll.search(10))          # True
    print("Search 99:", ll.search(99))          # False

    ll.delete(10)
    print("After deleting 10:", ll.display())   # [5, 20]
