"""
Subset Generation (Backtracking)
---------------------------------
Generate all possible subsets (the power set) of a given list.

Backtracking is used to explore each inclusion/exclusion of elements recursively.

Time Complexity: O(2^n)
Space Complexity: O(2^n) – for storing all subsets
"""

def generate_subsets(nums):
    def backtrack(start, path):
        result.append(path[:])  # Add a copy of the current subset
        for i in range(start, len(nums)):
            path.append(nums[i])             # Choose
            backtrack(i + 1, path)           # Explore
            path.pop()                       # Un-choose (backtrack)

    result = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    subsets = generate_subsets(nums)
    print(f"Subsets of {nums}:")
    for subset in subsets:
        print(subset)
