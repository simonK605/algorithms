"""
Min Heap (Priority Queue)
---------------------------
A Min Heap is a complete binary tree where each node is smaller than its children.
The smallest element is always at the root.

Supported Operations:
- insert(value)
- extract_min()
- peek()
- display()

Time Complexity:
- Insert: O(log n)
- Extract Min: O(log n)
- Peek: O(1)

Space Complexity: O(n)
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract_min(self):
        """Remove and return the minimum element."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_down(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def peek(self):
        """Return the smallest element without removing it."""
        return self.heap[0] if self.heap else None

    def display(self):
        """Return the internal heap array."""
        return self.heap


if __name__ == "__main__":
    h = MinHeap()
    h.insert(20)
    h.insert(5)
    h.insert(15)
    h.insert(22)
    h.insert(1)

    print("Min Heap:", h.display())         # [1, 5, 15, 22, 20]
    print("Peek:", h.peek())               # 1
    print("Extracted Min:", h.extract_min())  # 1
    print("Heap after extraction:", h.display())  # [5, 20, 15, 22]
