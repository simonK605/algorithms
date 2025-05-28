"""
Heap Sort Algorithm
Time Complexity: O(n log n)
Description: Converts list to a heap, then repeatedly extracts the max element.
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    print(heap_sort([4, 10, 3, 5, 1]))
