"""
Least Common Multiple (Math)
------------------------------
The Least Common Multiple (LCM) of two integers a and b is the smallest positive integer
that is divisible by both a and b.

Formula:
LCM(a, b) = abs(a * b) // GCD(a, b)

Time Complexity: O(log(min(a, b))) — due to GCD calculation
Space Complexity: O(1)
"""

import math

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


if __name__ == "__main__":
    pairs = [
        (4, 5),
        (10, 15),
        (0, 7),
        (21, 6),
        (100, 25)
    ]

    for a, b in pairs:
        print(f"LCM({a}, {b}) = {lcm(a, b)}")
