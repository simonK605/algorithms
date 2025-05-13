"""
Linear Search (Brute Force)
Time Complexity: O(n)
"""

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1  # Not found

if __name__ == "__main__":
    arr = [3, 5, 1, 8, 4]
    print(linear_search(arr, 8))  # Output: 3
    print(linear_search(arr, 6))  # Output: -1