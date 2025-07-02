"""
Sudoku Solver (Backtracking)
-----------------------------
Solves a given 9x9 Sudoku puzzle by filling in empty cells ('.') such that:
- Each row contains digits 1–9 with no repetition.
- Each column contains digits 1–9 with no repetition.
- Each 3×3 subgrid contains digits 1–9 with no repetition.

Time Complexity: O(9^(n*n)) in the worst case
Space Complexity: O(1) — the board is modified in-place
"""

def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 box
        box_row = 3 * (row // 3)
        box_col = 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'  # backtrack
                    return False  # no valid number found
        return True  # board completely filled

    backtrack()


if __name__ == "__main__":
    puzzle = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print("Input Sudoku:")
    for row in puzzle:
        print(" ".join(row))

    solve_sudoku(puzzle)

    print("\nSolved Sudoku:")
    for row in puzzle:
        print(" ".join(row))
