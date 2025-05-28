"""
Queue (FIFO - First In, First Out)
Operations:
- Enqueue: O(1)
- Dequeue: O(1)
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        return not self.queue

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.peek())     # 2
