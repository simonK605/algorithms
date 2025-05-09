"""
Exponential Search (Divide and Conquer)
Time Complexity: O(log i) where i is the position of the target
Requires: Sorted array
"""

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, len(arr) - 1))

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(exponential_search(arr, 6))  # Output: 5
    print(exponential_search(arr, 11)) # Output: -1
