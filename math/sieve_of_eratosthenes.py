"""
Sieve of Eratosthenes (Math - Prime Generation)
------------------------------------------------
An efficient algorithm to find all prime numbers less than or equal to a given number `n`.

Idea:
- Mark all numbers as prime initially
- Starting from 2, eliminate all multiples of each prime

Time Complexity: O(n log log n)
Space Complexity: O(n)

Use Cases:
- Fast prime number generation
- Useful in number theory problems, cryptography
"""

def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n (inclusive)."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n + 1, i):
                is_prime[multiple] = False

    return [i for i, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    n = 50
    primes = sieve_of_eratosthenes(n)
    print(f"Primes up to {n}:")
    print(primes)
