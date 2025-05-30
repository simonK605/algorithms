"""
Shell Sort
Time Complexity: Depends on gap sequence (Best: O(n log n), Worst: O(n^2))
Description: Generalization of insertion sort that allows swapping far-apart elements.
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

if __name__ == "__main__":
    print(shell_sort([12, 34, 54, 2, 3]))
