"""
Longest Increasing Subsequence (LIS)
Find length of the longest increasing subsequence in an array.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
