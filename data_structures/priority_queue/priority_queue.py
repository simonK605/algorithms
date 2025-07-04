"""
Priority Queue (with Min-Heap)
-------------------------------
A Priority Queue is a data structure where each element is associated
with a priority, and elements are dequeued in order of their priority
(lowest number = highest priority in a min-heap).

This example uses Python's `heapq` module.

Time Complexity:
- Insertion: O(log n)
- Removal (pop): O(log n)
- Peek: O(1)

Use Cases:
- CPU Scheduling
- Pathfinding (Dijkstra's Algorithm)
- A* Search
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0  # to handle tie-breaking in priority

    def push(self, priority, item):
        """
        Add an item with a given priority.
        Lower priority value means higher priority.
        """
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        """
        Remove and return the item with the highest priority.
        """
        if self._heap:
            return heapq.heappop(self._heap)[-1]
        raise IndexError("pop from empty priority queue")

    def peek(self):
        """
        Return the item with the highest priority without removing it.
        """
        if self._heap:
            return self._heap[0][-1]
        return None

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(3, "email support")
    pq.push(1, "emergency bug fix")
    pq.push(2, "code review")

    print("Next task:", pq.peek())  # emergency bug fix

    while not pq.is_empty():
        print("Handling task:", pq.pop())
