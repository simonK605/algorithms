"""
Minimum Path Sum (Dynamic Programming)
----------------------------------------
Given a `m x n` grid filled with non-negative numbers,
find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.

You can only move either down or right at any point in time.

Time Complexity: O(m * n)
Space Complexity: O(m * n) (can be reduced to O(n) with optimization)
"""

def min_path_sum(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize starting point
    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print("Grid:")
    for row in grid:
        print(row)
    print("\nMinimum Path Sum:", min_path_sum(grid))  # Output: 7
