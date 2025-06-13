"""
Longest Common Subsequence (LCS)
Find the length of the longest subsequence common to two strings.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[m][n]


if __name__ == "__main__":
    print(lcs("abcde", "ace"))  # Output: 3 ("ace")
