"""
Climbing Stairs (DP)
You can climb 1 or 2 steps. Count the distinct ways to reach the top.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    print(climb_stairs(5))  # Output: 8
