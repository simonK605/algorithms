"""
Permutations (Recursion + Backtracking)
----------------------------------------
Generate all possible permutations of a list of distinct elements.

Example:
Input: [1, 2, 3]
Output: [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

Time Complexity: O(n!) — total number of permutations
Space Complexity: O(n) — recursion depth and current permutation
"""

def generate_permutations(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    result = []
    backtrack([], [False] * len(nums))
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    permutations = generate_permutations(nums)
    print(f"Permutations of {nums}:")
    for p in permutations:
        print(p)
