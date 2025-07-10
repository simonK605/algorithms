"""
Decode Ways (Dynamic Programming)
----------------------------------
A message containing letters from A-Z is encoded as follows:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

Given a string of digits, return the number of ways it can be decoded.

Example:
Input: "226"
Output: 3
Explanation: "2 2 6" -> "BBF", "22 6" -> "VF", "2 26" -> "BZ"

Time Complexity: O(n)
Space Complexity: O(n) or O(1) with optimization
"""

def num_decodings(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1  # empty string
    dp[1] = 1  # first character (already checked not '0')

    for i in range(2, n + 1):
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2:i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    test_cases = [
        "12",     # 2: "AB", "L"
        "226",    # 3: "BBF", "BZ", "VF"
        "06",     # 0: invalid
        "11106",  # 2: "AAJF", "KJF"
        "0",      # 0: invalid
        "1",      # 1: "A"
    ]

    for s in test_cases:
        print(f"Input: '{s}' → Ways to decode: {num_decodings(s)}")
