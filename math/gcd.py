"""
GCD (Greatest Common Divisor)
Time Complexity: O(log(min(a, b)))
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(gcd(48, 18))  # Output: 6
