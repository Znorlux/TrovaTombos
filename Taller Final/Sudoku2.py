def is_valid(matrix):
    target_sum = 16
    for row in matrix:
        if sum(row) != target_sum:
            return False
    for col in range(len(matrix[0])):
        if sum(matrix[row][col] for row in range(len(matrix))) != target_sum:
            return False
    return True

def solve_sudoku(matrix):
    def backtrack(row, col):
        if row == len(matrix):
            return is_valid(matrix)
        
        if matrix[row][col] is not None:
            next_row, next_col = (row, col + 1) if col < len(matrix[0]) - 1 else (row + 1, 0)
            return backtrack(next_row, next_col)
        
        for num in range(1, 15):
            matrix[row][col] = num
            next_row, next_col = (row, col + 1) if col < len(matrix[0]) - 1 else (row + 1, 0)
            if backtrack(next_row, next_col):
                return True
            matrix[row][col] = None
        
        return False

    if backtrack(0, 0):
        return matrix
    else:
        return None

matrix = [[3, 6, 7], 
         [None, 7, None], # = Todas las sumas en vertical y en horizontal deben dar 16
        [8, None, 5]]

result = solve_sudoku(matrix)

if result:
    for row in result:
        print(row)
else:
    print("No solution found.")
