"""
Fibonacci (Bottom-Up with Tabulation)
Time Complexity: O(n)
Space Complexity: O(n)
"""

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


if __name__ == "__main__":
    print(fibonacci(10))  # Output: 55
