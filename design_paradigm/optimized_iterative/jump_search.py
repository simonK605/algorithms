"""
Jump Search (Optimized Iterative)
Time Complexity: O(√n)
Requires: Sorted array
"""

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(jump_search(arr, 7))  # Output: 3
    print(jump_search(arr, 4))  # Output: -1
