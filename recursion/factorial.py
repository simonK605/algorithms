"""
Factorial (Recursion)
Time Complexity: O(n)
Space Complexity: O(n) – due to call stack
"""

def factorial(n):
    """
    Returns the factorial of n.
    n! = n * (n-1) * ... * 1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1
