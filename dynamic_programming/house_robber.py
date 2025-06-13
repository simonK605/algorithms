"""
House Robber
You cannot rob two adjacent houses. Maximize the amount you can steal.

Time Complexity: O(n)
Space Complexity: O(1) – space-optimized
"""

def house_robber(nums):
    prev = curr = 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


if __name__ == "__main__":
    print(house_robber([2, 7, 9, 3, 1]))  # Output: 12 (rob 2 + 9 + 1)
