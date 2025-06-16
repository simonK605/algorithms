"""
Fibonacci (Recursion)
Time Complexity: O(2^n)
Space Complexity: O(n) – call stack
Note: This is not efficient for large n. Use DP for better performance.
"""

def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    fib(0) = 0, fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(0))   # Output: 0
    print(fibonacci(1))   # Output: 1
    print(fibonacci(6))   # Output: 8
