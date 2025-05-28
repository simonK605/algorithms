"""
Insertion Sort Algorithm
Time Complexity: O(n^2)
Description: Builds the sorted array one element at a time.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6]))
