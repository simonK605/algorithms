"""
Priority Queue using heapq (Min-Heap)
---------------------------------------
The heapq module in Python provides an efficient way to implement
priority queues using binary heaps.

By default, heapq implements a min-heap.

Time Complexity:
- Insert: O(log n)
- Pop (smallest): O(log n)
- Peek (min): O(1)

Use Cases:
- Task scheduling
- Shortest path algorithms (e.g., Dijkstra)
- Event simulation
"""

import heapq

def min_heap_example():
    print("Min-Heap Example:")
    heap = []
    nums = [5, 1, 9, 3, 7]

    for num in nums:
        heapq.heappush(heap, num)  # O(log n)

    print("Heap structure:", heap)
    print("Smallest element:", heapq.heappop(heap))  # O(log n)
    print("Next smallest:", heapq.heappop(heap))


def max_heap_example():
    print("\nMax-Heap Example (simulated using negatives):")
    heap = []
    nums = [5, 1, 9, 3, 7]

    for num in nums:
        heapq.heappush(heap, -num)  # use negatives to simulate max-heap

    print("Max-Heap structure (in negated form):", heap)
    print("Largest element:", -heapq.heappop(heap))  # reverse sign back
    print("Next largest:", -heapq.heappop(heap))


def priority_queue_with_tuples():
    print("\nPriority Queue with Tuples:")
    tasks = []
    heapq.heappush(tasks, (3, "write code"))
    heapq.heappush(tasks, (1, "fix bugs"))
    heapq.heappush(tasks, (2, "submit report"))

    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"Task: {task} (priority {priority})")


if __name__ == "__main__":
    min_heap_example()
    max_heap_example()
    priority_queue_with_tuples()
