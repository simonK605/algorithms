"""
Selection Sort
Time Complexity: O(n^2)
Description: Selects the minimum element and places it at the beginning.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the smallest element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))
