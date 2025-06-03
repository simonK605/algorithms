"""
Ternary Search (Divide and Conquer)
Time Complexity: O(log₃ n)
Only works for unimodal functions or sorted arrays.
"""

def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

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

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print(ternary_search(arr, 9))  # Output: 4
