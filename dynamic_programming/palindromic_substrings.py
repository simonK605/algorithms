"""
Palindromic Substrings (Dynamic Programming)
---------------------------------------------
Given a string `s`, return the total number of palindromic substrings in it.

A substring is a contiguous sequence of characters, and a palindrome
reads the same forward and backward.

Example:
Input: "abc" → Output: 3  (a, b, c)
Input: "aaa" → Output: 6  (a, a, a, aa, aa, aaa)

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    # Single-character substrings are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Substrings of length 3 or more
    for length in range(3, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1  # ending index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count


if __name__ == "__main__":
    test_cases = ["abc", "aaa", "abba", "racecar", "aabaa"]

    for s in test_cases:
        print(f"Input: '{s}' → Palindromic substrings: {count_palindromic_substrings(s)}")
