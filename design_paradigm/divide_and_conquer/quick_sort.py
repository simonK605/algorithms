"""
Quick Sort (Divide and Conquer)
--------------------------------
Quick Sort is an efficient, in-place sorting algorithm.
It selects a pivot, partitions the array into elements
less than and greater than the pivot, and recursively sorts them.

Time Complexity:
- Best & Average: O(n log n)
- Worst: O(n^2) (rare, happens when the pivot is the smallest/largest)

Space Complexity: O(log n) for recursion stack (in-place sort)

Stable Sort: No
"""

def quick_sort(arr):
    """Sort the array using quick sort and return the result."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # or choose first/last/random for optimization
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # keep equal for stability-like behavior
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    data = [29, 10, 14, 37, 13, 13]
    print("Original: ", data)
    sorted_data = quick_sort(data)
    print("Sorted:   ", sorted_data)
