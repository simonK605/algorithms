"""
Generate Parentheses (Recursion + Backtracking)
------------------------------------------------
Given `n` pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Time Complexity: O(2^n) for generation, but number of valid combinations is the nth Catalan number: O(4^n / √n)
Space Complexity: O(n) for the recursion stack (excluding output)

Approach:
- Use backtracking to build the string step-by-step
- Add '(' if we still have some left
- Add ')' if it won't unbalance the expression
"""

def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append("".join(current))
            return

        if open_count < n:
            current.append('(')
            backtrack(current, open_count + 1, close_count)
            current.pop()

        if close_count < open_count:
            current.append(')')
            backtrack(current, open_count, close_count + 1)
            current.pop()

    result = []
    backtrack([], 0, 0)
    return result


if __name__ == "__main__":
    n = 3
    combinations = generate_parentheses(n)
    print(f"Valid combinations of {n} pairs of parentheses:")
    for combo in combinations:
        print(combo)
