"""
Deque (Double-Ended Queue)
Operations:
- Append Left / Right: O(1)
- Pop Left / Right: O(1)
"""

from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def append_left(self, item):
        self.deque.appendleft(item)

    def append_right(self, item):
        self.deque.append(item)

    def pop_left(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.popleft()

    def pop_right(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop()

    def peek_left(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[0]

    def peek_right(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[-1]

    def is_empty(self):
        return not self.deque

    def size(self):
        return len(self.deque)


if __name__ == "__main__":
    d = Deque()
    d.append_left(1)
    d.append_right(2)
    print(d.pop_left())   # 1
    print(d.pop_right())  # 2
