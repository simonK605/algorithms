"""
Find Maximum Element in List (Recursion)
Time Complexity: O(n)
Space Complexity: O(n)
"""

def find_max(arr):
    """
    Recursively finds the maximum element in an array.
    """
    if len(arr) == 0:
        raise ValueError("Empty list has no maximum")
    if len(arr) == 1:
        return arr[0]
    max_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_rest else max_rest


if __name__ == "__main__":
    print(find_max([3, 1, 9, 4, 2]))  # Output: 9
