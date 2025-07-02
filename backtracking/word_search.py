"""
Word Search (Backtracking)
---------------------------
Given a 2D board and a word, return True if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically),
but the same letter cell may not be used more than once.

Time Complexity: O(m * n * 4^L)
    - m*n: each cell as a starting point
    - 4^L: max branching factor for word of length L
Space Complexity: O(L) – recursion depth
"""

def exist(board, word):
    rows, cols = len(board), len(board[0])
    visited = set()

    def backtrack(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or (r, c) in visited):
            return False

        visited.add((r, c))
        res = (backtrack(r + 1, c, i + 1) or
               backtrack(r - 1, c, i + 1) or
               backtrack(r, c + 1, i + 1) or
               backtrack(r, c - 1, i + 1))
        visited.remove((r, c))
        return res

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True
    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    print(f"Word '{word}' exists in board:", exist(board, word))  # Output: True

    word2 = "SEE"
    print(f"Word '{word2}' exists in board:", exist(board, word2))  # Output: True

    word3 = "ABCB"
    print(f"Word '{word3}' exists in board:", exist(board, word3))  # Output: False
