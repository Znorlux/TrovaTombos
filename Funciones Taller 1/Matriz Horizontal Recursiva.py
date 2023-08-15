def matriz_horizontal(matrix, sentido, row_index=0, col_index=0):
    if row_index >= 0 and row_index < len(matrix): #Verificiamos si estamos en los limites de la matriz o ya la acabamos (caso base)
        if col_index >= 0 and col_index < len(matrix[row_index]):
            print(matrix[row_index][col_index])
            if sentido == "derecha":
                matriz_horizontal(matrix,sentido, row_index, col_index + 1)
            else:
                matriz_horizontal(matrix, sentido, row_index, col_index - 1)
        else:

            if sentido == "derecha":
                matriz_horizontal(matrix, "izquierda", row_index + 1, len(matrix[row_index + 1]) - 1 )
            else:
                matriz_horizontal(matrix, "derecha", row_index + 1, 0)
    else:
        return

m = [
    [1, 2, 3, 4, 5],
    [10, 9, 8, 7, 99],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16]
]

matriz_horizontal(m, "derecha")#El primer indice de columna y fila será siempre 0