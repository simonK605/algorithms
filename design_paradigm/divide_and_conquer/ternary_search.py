"""
Ternary Search (Divide and Conquer)
Time Complexity: O(log₃ n)
Requires: Sorted array, unimodal function (for optimization problems)
"""

def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1  # Not found

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(ternary_search(arr, 7))  # Output: 3
    print(ternary_search(arr, 6))  # Output: -1
