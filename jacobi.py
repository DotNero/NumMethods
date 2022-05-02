import numpy as np

import config
import diagmatrix
import accurancy
import matplotlib as mpl

n = config.n
matrix:np = diagmatrix.rdiagmatrix(n)
fv:np = diagmatrix.fvector(n)
import math
import copy

# Пробные данные для уравнения A*X = B
# x = [1.10202, 0.99091, 1.01111]


matrix = diagmatrix.matrix(config.n)
fvec = diagmatrix.fvector(config.n)



# Проверка матрицы коэффициентов на корректность
# def isCorrectArray(matrix):
#     for row in range(n):
#         if (len(a[row]) != len(b)):
#             print('Не соответствует размерность')
#             return False

    # for row in range(n):
    #     if (a[row][row] == 0):
    #         print('Нулевые элементы на главной диагонали')
    #         return False
    # return True


# Условие завершения программы на основе вычисления
# расстояния между соответствующими элементами соседних
# итераций в методе решения
def isNeedToComplete(x_new, x_old):
    eps = config.eps
    accurancy.accuracyparametr(x_new, x_old)



# Процедура решения
def solution(matrix, fvec):

        x = [1 for k in range(0,n)]  # начальное приближение корней

        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = config.maxiter  # максимально допустимое число итераций
        while (numberOfIter < MAX_ITER):

            x_prev = copy.deepcopy(x)

            for k in range(0, n):
                S = 0
                for j in range(0, n):
                    if (j != k): S = S + matrix[k,j] * x[j]
                x[k] = fvec[k] / matrix[k,k] - S / matrix[k,k]

            if isNeedToComplete(x_prev, x):  # проверка на выход
                break

            numberOfIter += 1

        print('Количество итераций на решение: ', numberOfIter)

        return x
