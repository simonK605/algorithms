"""
Rabin-Karp Substring Search Algorithm
--------------------------------------
The Rabin-Karp algorithm uses hashing to find any one of a set of pattern strings in a text.

Main Idea:
- Use a rolling hash to quickly compare substring hashes with the pattern hash.
- If hashes match, do an exact comparison to verify (due to hash collisions).

Time Complexity:
- Average: O(n + m) where n = length of text, m = length of pattern
- Worst-case: O(n * m) (due to collisions, rare in practice)

Hashing Base: 256 (number of characters in extended ASCII)
Modulus: A large prime number to reduce collisions
"""

def rabin_karp(text, pattern):
    if not pattern or not text or len(pattern) > len(text):
        return []

    base = 256  # base for hashing (number of possible characters)
    mod = 101   # a prime number to reduce collisions

    n, m = len(text), len(pattern)
    h = 1  # high-order digit weight

    for _ in range(m - 1):
        h = (h * base) % mod

    pattern_hash = 0
    window_hash = 0

    # Initial hash values for pattern and first window
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    result = []

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if window_hash < 0:
                window_hash += mod

    return result


if __name__ == "__main__":
    text = "abedabcabcabcd"
    pattern = "abc"
    matches = rabin_karp(text, pattern)
    print(f"Pattern '{pattern}' found at positions: {matches}")
