def maximumPath(N, Matrix):
    # Inicializar una tabla de memorización para almacenar los valores máximos de suma
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Llenar la última fila de la tabla de memorización con valores de la fila inferior de la matriz
    for i in range(N):
        dp[N-1][i] = Matrix[N-1][i]

    # Comenzando desde la penúltima fila y avanzando hacia arriba
    for i in range(N - 2, -1, -1):
        for j in range(N):
            # Calcular la suma de ruta máxima para la celda actual considerando tres movimientos posibles
            dp[i][j] = Matrix[i][j] + max(dp[i + 1][j], dp[i + 1][j - 1] if j > 0 else 0, dp[i + 1][j + 1] if j < N - 1 else 0)

    # Encuentra el valor máximo en la primera fila de la tabla de memorización.
    max_path_sum = max(dp[0])

    return max_path_sum

# Ejemplo 1
N1 = 2
Matrix1 = [[348, 391], [618, 193]]
print(maximumPath(N1, Matrix1))  # Resultado: 1009

# Ejemplo 2
N2 = 2
Matrix2 = [[3, 3], [3, 3]]
print(maximumPath(N2, Matrix2))  # resultado: 6