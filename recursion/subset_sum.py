"""
Subset Sum Problem (Recursion + Backtracking)
----------------------------------------------
Given a list of integers and a target sum, determine all subsets of numbers
that add up exactly to the target.

Example:
Input: nums = [2, 3, 5], target = 8
Output: [[3, 5]]

Time Complexity: O(2^n)
Space Complexity: O(n) for recursion stack

Approach:
- Try including and excluding each number
- Backtrack once the sum exceeds target or we've used all elements
"""

def subset_sum(nums, target):
    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current, total + nums[i])
            current.pop()

    result = []
    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target = 9
    subsets = subset_sum(nums, target)
    print(f"Subsets of {nums} that sum to {target}:")
    for subset in subsets:
        print(subset)
