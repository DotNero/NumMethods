import numpy as np

import config
import diagmatrix
import accurancy
import copy
import math
import iterationdynamics
import matplotlib as mpl

n = config.n
# Пробные данные для уравнения A*X = B
# x = [1.10202, 0.99091, 1.01111]
matrix:np = diagmatrix.matrixofdiagonals(config.n)
fvec:np = diagmatrix.matrixofdiagonals(config.n)



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





# Процедура решения
def solution(matrix, fvec):
        x = np.ones((n))
        I_D = iterationdynamics.IterationDynamic(x, x)
        # начальное приближение корней
        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = config.maxiter  # максимально допустимое число итераций
        while (I_D._itmark < MAX_ITER):
            #x_prev = copy.deepcopy(x)
            I_D.x_old = I_D.x_new
            for k in range(n):
                S = 0
                for j in range(n):
                    if (j != k): S = S + matrix[k,j] * I_D.x_new[j]
                I_D.x_new[k] = fvec[k] / matrix[k, k] - S / matrix[k, k]

            if I_D.isNeedToComplete():  # проверка на выход
                break
            I_D.state_version(numberOfIter)
            numberOfIter += 1


        print('Количество итераций на решение: ', numberOfIter)
        return I_D

