"""
Quick Sort (Divide and Conquer)
Time Complexity: Average O(n log n), Worst O(n²)
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([5, 2, 4, 1, 3]))
