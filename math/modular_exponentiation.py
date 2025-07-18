"""
Modular Exponentiation (Math)
------------------------------
Computes (base^exponent) % modulus efficiently using the binary exponentiation method.

Why?
- Naively computing `base ** exponent` can cause overflow or be too slow.
- Modular exponentiation is used in cryptography (e.g., RSA), primality tests, etc.

Time Complexity: O(log exponent)
Space Complexity: O(1)

Function signature:
modular_pow(base, exponent, modulus) -> int
"""

def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0  # any number mod 1 is 0
    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result


if __name__ == "__main__":
    test_cases = [
        (2, 10, 1000),     # 1024 % 1000 = 24
        (3, 13, 7),        # 3^13 % 7 = 5
        (10, 0, 999),      # 10^0 % 999 = 1
        (7, 256, 13),      # large exponent
        (5, 117, 19),      # used in RSA
    ]

    for base, exp, mod in test_cases:
        result = modular_pow(base, exp, mod)
        print(f"({base}^{exp}) % {mod} = {result}")
