#!/usr/bin/python3


import sys

def is_safe(board, row, col, N):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    if col == N:
        # Found a solution, print it
        for row in range(N):
            for col in range(N):
                if board[row][col] == 1:
                    print(col + 1, end=" ")
        print()
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen and recurse
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            # Backtrack (remove the queen)
            board[i][col] = 0
    return res

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("No solution exists")
        return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
