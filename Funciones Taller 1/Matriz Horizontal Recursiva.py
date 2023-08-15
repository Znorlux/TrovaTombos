def matriz_horizontal(matrix, sentido, row_index=0, col_index=0):
    if row_index >= 0 and row_index < len(matrix): #Verificiamos si el indice de fila en el que vamos, aun no se ha pasado de la longitud de la mtriz
        if col_index >= 0 and col_index < len(matrix[row_index]):#Verificamos lo mismo con las columnas
            print(matrix[row_index][col_index])#Imprimimos el elemento en el indice en el que vayamos de la matriz
            #Para continuar necesitamos saber si debemos ir a la derecha o a la izquierda
            if sentido == "derecha":
                matriz_horizontal(matrix,sentido, row_index, col_index + 1)
            else:
                matriz_horizontal(matrix, sentido, row_index, col_index - 1)
        else:
            #Cuando el indice de las filas pase la longitud de la matriz, significa que ya acabamos de recorrer esa fila
            #El sentido cambiará cuando acabemos de recorrer una fila
            if sentido == "derecha":
                matriz_horizontal(matrix, "izquierda", row_index + 1, len(matrix[row_index + 1]) - 1 )
            else:
                matriz_horizontal(matrix, "derecha", row_index + 1, 0)
    else:
        return

m = [
    [1, 2, 3, 4, 5],
    [10, 9, 8, 7, 6],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16]
]

matriz_horizontal(m, "derecha")#El primer indice de columna y fila será siempre 0
