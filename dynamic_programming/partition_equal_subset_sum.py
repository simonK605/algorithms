"""
Partition Equal Subset Sum
Determine if the array can be partitioned into two subsets with equal sum.

Time Complexity: O(n * sum/2)
Space Complexity: O(sum/2)
"""

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]


if __name__ == "__main__":
    print(can_partition([1, 5, 11, 5]))  # Output: True
