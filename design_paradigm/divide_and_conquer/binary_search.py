"""
Binary Search (Divide and Conquer)
Time Complexity: O(log n)
"""


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(binary_search(arr, 4))  # Output: 3
    print(binary_search(arr, 9))  # Output: -1
