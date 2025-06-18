"""
Power Calculation (Recursion)
Time Complexity: O(n)
Space Complexity: O(n)
"""

def power(base, exponent):
    """
    Returns base raised to the power exponent using recursion.
    Assumes exponent is a non-negative integer.
    """
    if exponent < 0:
        raise ValueError("This function does not support negative exponents")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


if __name__ == "__main__":
    print(power(2, 3))  # Output: 8
    print(power(5, 0))  # Output: 1
