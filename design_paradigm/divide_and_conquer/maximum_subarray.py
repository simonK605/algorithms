"""
Maximum Subarray (Divide and Conquer)
--------------------------------------
Given an array of integers, find the contiguous subarray with the largest sum.

This is the Divide and Conquer approach (not Kadane's algorithm).

Time Complexity: O(n log n)
Space Complexity: O(log n) due to recursion stack
"""

def max_crossing_subarray(arr, low, mid, high):
    """Find maximum subarray sum that crosses the midpoint."""
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def max_subarray(arr, low, high):
    """Recursive divide and conquer method."""
    if low == high:
        return arr[low]

    mid = (low + high) // 2
    left_max = max_subarray(arr, low, mid)
    right_max = max_subarray(arr, mid + 1, high)
    cross_max = max_crossing_subarray(arr, low, mid, high)

    return max(left_max, right_max, cross_max)


def find_maximum_subarray(arr):
    """Wrapper function."""
    if not arr:
        return 0
    return max_subarray(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [13, -3, -25, 20, -3, -16, -23, 18,
           20, -7, 12, -5, -22, 15, -4, 7]

    print("Array:", arr)
    max_sum = find_maximum_subarray(arr)
    print("Maximum Subarray Sum:", max_sum)  # Output: 43
