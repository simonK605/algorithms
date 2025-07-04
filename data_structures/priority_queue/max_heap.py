"""
Max Heap Implementation (Manual)
---------------------------------
A Max-Heap is a complete binary tree where each node is greater than or equal
to its children. The largest element is always at the root.

Supported Operations:
- insert
- extract_max
- peek (get max)
- heapify

Time Complexity:
- insert: O(log n)
- extract_max: O(log n)
- peek: O(1)

Space Complexity: O(n)
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def extract_max(self):
        """Remove and return the maximum element."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_down(self, i):
        max_index = i
        l = self._left(i)
        r = self._right(i)

        if l < len(self.heap) and self.heap[l] > self.heap[max_index]:
            max_index = l
        if r < len(self.heap) and self.heap[r] > self.heap[max_index]:
            max_index = r

        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self._sift_down(max_index)

    def peek(self):
        """Return the maximum element without removing it."""
        if not self.heap:
            return None
        return self.heap[0]

    def display(self):
        """Return the heap as a list."""
        return self.heap


if __name__ == "__main__":
    h = MaxHeap()
    h.insert(10)
    h.insert(30)
    h.insert(20)
    h.insert(5)
    h.insert(100)

    print("Heap:", h.display())          # [100, 30, 20, 5, 10]
    print("Max element:", h.peek())      # 100
    print("Extract max:", h.extract_max())  # 100
    print("Heap after extraction:", h.display())  # [30, 10, 20, 5]
