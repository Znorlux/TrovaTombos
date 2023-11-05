# Función que verifica si la matriz cumple con la condición de que todas las sumas en filas y columnas sean iguales a 14.
def is_valid(matrix):
    target_sum = 14
    for row in matrix:
        if sum(row) != target_sum:  # Verifica si la suma de una fila no es igual a 14.
            return False
    for col in range(len(matrix[0])):
        if sum(matrix[row][col] for row in range(len(matrix))) != target_sum:  # Verifica si la suma de una columna no es igual a 14.
            return False
    return True

# Función principal para resolver el Sudoku utilizando backtracking.
def solve_sudoku(matrix):
    def backtrack(row, col):
        if row == len(matrix):  # Si hemos llegado al final de la matriz, se verifica si es válida.
            return is_valid(matrix)
        
        if matrix[row][col] is not None:  # Si la celda ya tiene un valor, pasamos a la siguiente celda.
            next_row, next_col = (row, col + 1) if col < len(matrix[0]) - 1 else (row + 1, 0)
            return backtrack(next_row, next_col)
        
        for num in range(1, 15):  # Probamos numeros del 1 al 14 en la celda actual.
            matrix[row][col] = num
            next_row, next_col = (row, col + 1) if col < len(matrix[0]) - 1 else (row + 1, 0)
            if backtrack(next_row, next_col):  # Llamada recursiva para verificar si la solución es válida.
                return True
            matrix[row][col] = None  # Si la solución no es válida, restauramos la celda y probamos otro número.
        
        return False

    if backtrack(0, 0):  # Llamamos a la función de backtracking para encontrar una solución.
        return matrix
    else:
        return None

matrix = [[5, None, 2], [8, 5, None], [None, 2, None]]

result = solve_sudoku(matrix)  

if result:
    for row in result:
        print(row)  
else:
    print("No se encontró solucion")
