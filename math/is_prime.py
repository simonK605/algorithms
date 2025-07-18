"""
Prime Number Check (Math)
---------------------------
Check if a given number is a prime number.

A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Optimized approach:
- Only check divisibility up to sqrt(n)
- Skip even numbers after 2

Time Complexity: O(√n)
Space Complexity: O(1)
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 19, 20, 97, 100]

    for number in test_numbers:
        print(f"{number} → {'Prime' if is_prime(number) else 'Not Prime'}")
