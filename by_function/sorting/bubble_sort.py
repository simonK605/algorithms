"""
Bubble Sort Algorithm
Time Complexity: O(n^2)
Description: Repeatedly swaps adjacent elements if they are in the wrong order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
