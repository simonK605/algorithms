"""
Sum of Array Elements (Recursion)
Time Complexity: O(n)
Space Complexity: O(n) – due to recursive calls
"""

def sum_array(arr):
    """
    Returns the sum of all elements in an array using recursion.
    """
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5]))  # Output: 15
