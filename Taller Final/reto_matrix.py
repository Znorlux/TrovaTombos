# -*- coding: utf-8 -*-
"""reto matrix

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kRqF-058bbGzi038oj05cMRgF85HmxaU
"""

def maximumPath(self,N, Matrix):
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        dp[N-1][i] = Matrix[N-1][i]

    for i in range(N - 2, -1, -1):
        for j in range(N):
            dp[i][j] = Matrix[i][j] + max(dp[i + 1][j], dp[i + 1][j - 1] if j > 0 else 0, dp[i + 1][j + 1] if j < N - 1 else 0)

    max_path_sum = max(dp[0])

    return max_path_sum