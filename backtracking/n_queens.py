"""
N-Queens Problem (Backtracking)
--------------------------------
Place N queens on an N×N chessboard such that no two queens threaten each other.

This implementation finds and returns all valid solutions.

Time Complexity: O(N!)
Space Complexity: O(N^2) for storing board states
"""

def solve_n_queens(n):
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        return (col not in cols and
                (row - col) not in diagonals and
                (row + col) not in anti_diagonals)

    def place_queen(row, state):
        if row == n:
            result.append(["".join(r) for r in state])
            return

        for col in range(n):
            if is_safe(row, col, diagonals, anti_diagonals, cols):
                state[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                place_queen(row + 1, state)

                # Backtrack
                state[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

    result = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diagonals = set()
    anti_diagonals = set()

    place_queen(0, empty_board)
    return result


if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
    for solution in solutions:
        for row in solution:
            print(row)
        print()
