"""
Z Algorithm for Pattern Matching
----------------------------------
The Z algorithm computes an array Z where Z[i] represents the length of the longest
substring starting at i that is also a prefix of the string.

It is commonly used to search for a pattern in a text in linear time.

Time Complexity: O(n)
Space Complexity: O(n)

Usage:
- Combine pattern + special delimiter + text into one string
- Compute Z-array and check for pattern matches

Example:
Pattern: "abc"
Text: "xabcabzabc"
Combined: "abc$xabcabzabc"
"""

def calculate_z_array(s):
    n = len(s)
    Z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z


def z_algorithm_search(text, pattern):
    concat = pattern + "$" + text
    Z = calculate_z_array(concat)
    pattern_length = len(pattern)
    result = []

    for i in range(pattern_length + 1, len(Z)):
        if Z[i] == pattern_length:
            result.append(i - pattern_length - 1)  # Adjust index

    return result


if __name__ == "__main__":
    text = "abcxabcdabxabcdabcdabcy"
    pattern = "abcdabcy"
    matches = z_algorithm_search(text, pattern)
    print(f"Pattern '{pattern}' found at positions: {matches}")
