import numpy as np

def solution(matrix:np, vector:np, n):

    x = np.zeros((n))  # обнуление вектора решений
    print('Размерность матрицы: ', n, 'x', n)

    # Прямой ход
    v = np.zeros((n))
    u = np.zeros((n))
    # для первой 0-й строки
    v[0] = matrix[0,1] / (-matrix[0,0])
    u[0] = (- vector[0]) / (-matrix[0,0])
    for i in range(1, n - 1):  # заполняем за исключением 1-й и (n-1)-й строк матрицы
        v[i] = matrix[i,i+1] / (-matrix[i,i] - matrix[i,i-1] * v[i - 1])
        u[i] = (matrix[i,i-1] * u[i - 1] - vector[i]) / (-matrix[i,i] - matrix[i,i-1] * v[i - 1])
    # для последней (n-1)-й строки
    v[n - 1] = 0
    u[n - 1] = (matrix[n-1,n-2] * u[n - 2] - vector[n - 1]) / (-matrix[n-1,n-1] - matrix[n-1,n-2] * v[n - 2])

    print('Прогоночные коэффициенты v: ', 'v', v)
    print('Прогоночные коэффициенты u: ', 'u', u)

    # Обратный ход
    x[n - 1] = u[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = v[i - 1] * x[i] + u[i - 1]

    return x