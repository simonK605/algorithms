"""
Coin Change
Minimum number of coins to make up a given amount.

Time Complexity: O(amount * n)
Space Complexity: O(amount)
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))  # Output: 3 (5+5+1)
