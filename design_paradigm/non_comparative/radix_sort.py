"""
Radix Sort
Time Complexity: O(nk) where k is the number of digits
Description: Non-comparison sort. Works well for fixed-length integers.
"""

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
