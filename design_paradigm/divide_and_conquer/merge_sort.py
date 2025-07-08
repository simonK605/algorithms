"""
Merge Sort (Divide and Conquer)
--------------------------------
Merge Sort is a classic sorting algorithm based on divide and conquer.
It splits the array into halves, recursively sorts each half,
and then merges the sorted halves.

Time Complexity: O(n log n)
Space Complexity: O(n)

Stable Sort: Yes
"""

def merge_sort(arr):
    """Sort the array using merge sort and return the sorted result."""
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer (Merge)
    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Stable sort
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", data)
    sorted_data = merge_sort(data)
    print("Sorted:  ", sorted_data)
