"""
Interpolation Search (Heuristic + Divide and Conquer)
Time Complexity: O(log log n) in best case, O(n) in worst case
Requires: Sorted, uniformly distributed data
"""

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if pos >= len(arr):  # avoid index error
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    print(interpolation_search(arr, 30))  # Output: 2
    print(interpolation_search(arr, 25))  # Output: -1
