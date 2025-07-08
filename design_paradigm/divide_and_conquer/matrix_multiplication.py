"""
Matrix Multiplication (Divide and Conquer)
-------------------------------------------
This implementation multiplies two square matrices using divide and conquer.

Time Complexity: O(n^3) in the basic form
Space Complexity: O(n^2)

For improvement, you can implement Strassen's Algorithm (O(n^log7) ≈ O(n^2.81))
"""

def add_matrix(A, B):
    """Add two matrices element-wise."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    """Subtract matrix B from matrix A element-wise."""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(M):
    """Split a square matrix into four quadrants."""
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

def combine_quadrants(C11, C12, C21, C22):
    """Combine four quadrants into a single matrix."""
    top = [a + b for a, b in zip(C11, C12)]
    bottom = [a + b for a, b in zip(C21, C22)]
    return top + bottom

def multiply_matrices(A, B):
    """Multiply two matrices using divide and conquer."""
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = multiply_matrices(A11, B11)
    M2 = multiply_matrices(A12, B21)
    C11 = add_matrix(M1, M2)

    M3 = multiply_matrices(A11, B12)
    M4 = multiply_matrices(A12, B22)
    C12 = add_matrix(M3, M4)

    M5 = multiply_matrices(A21, B11)
    M6 = multiply_matrices(A22, B21)
    C21 = add_matrix(M5, M6)

    M7 = multiply_matrices(A21, B12)
    M8 = multiply_matrices(A22, B22)
    C22 = add_matrix(M7, M8)

    return combine_quadrants(C11, C12, C21, C22)


if __name__ == "__main__":
    # 2x2 matrices (must be square and power of 2 in this implementation)
    A = [[1, 2],
         [3, 4]]

    B = [[5, 6],
         [7, 8]]

    result = multiply_matrices(A, B)

    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nProduct A * B:")
    for row in result:
        print(row)
