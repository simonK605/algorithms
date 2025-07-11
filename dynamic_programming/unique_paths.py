"""
Unique Paths (Dynamic Programming)
-----------------------------------
A robot is located at the top-left corner of an `m x n` grid. It can only move either
down or right at any point in time. The robot is trying to reach the bottom-right corner.

How many possible unique paths are there?

Time Complexity: O(m * n)
Space Complexity: O(m * n) (can be optimized to O(n))
"""

def unique_paths(m, n):
    # Create a 2D dp table with m rows and n columns
    dp = [[1] * n for _ in range(m)]

    # Start from cell (1,1) and fill the table
    for i in range(1, m):
        for j in range(1, n):
            # The number of ways to reach this cell is the sum of
            # ways to reach from the top and from the left
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    m, n = 3, 7
    print(f"Grid size: {m} x {n}")
    print("Unique paths from top-left to bottom-right:", unique_paths(m, n))  # Output: 28
