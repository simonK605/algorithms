"""
Stack (LIFO - Last In, First Out)
Operations:
- Push: O(1)
- Pop: O(1)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())   # 3
    print(s.peek())  # 2
