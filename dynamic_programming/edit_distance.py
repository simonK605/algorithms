"""
Edit Distance (Levenshtein Distance)
Minimum operations to convert word1 into word2 using insert, delete, or replace.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i  # Delete all characters
    for j in range(n+1):
        dp[0][j] = j  # Insert all characters

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance("kitten", "sitting"))  # Output: 3
