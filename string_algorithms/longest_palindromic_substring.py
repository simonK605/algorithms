"""
Longest Palindromic Substring (Expand Around Center)
-----------------------------------------------------
Given a string s, return the longest palindromic substring in s.

Approach:
- For each character, try to expand outward (both odd and even length centers)
- Keep track of the maximum length and start index

Time Complexity: O(n^2)
Space Complexity: O(1)

Alternative algorithms:
- Dynamic Programming: O(n^2) time and space
- Manacher's Algorithm: O(n) time
"""

def longest_palindromic_substring(s):
    if not s:
        return ""

    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)     # Odd length palindrome
        expand(i, i + 1) # Even length palindrome

    return s[start:start + max_len]


if __name__ == "__main__":
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "forgeeksskeegfor"
    ]

    for text in test_cases:
        result = longest_palindromic_substring(text)
        print(f"Input: {text} → Longest Palindromic Substring: {result}")
