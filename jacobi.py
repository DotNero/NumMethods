import numpy as np

import config
import diagmatrix
import accurancy
import copy
import math
import iterationdynamics
import matplotlib as mpl

n = config.n
matrix:np = diagmatrix.rdiagmatrix(n)
fv:np = diagmatrix.fvector(n)



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
    #eps = config.eps
    #return(accurancy.accuracyparametr(x_new, x_old))
    I_D = iterationdynamics.IterationDynamic(x_new, x_old)
    return(I_D.accuracyget())



# Процедура решения
def solution(matrix, fvec):
        I_D = iterationdynamics.IterationDynamic()
        x = [1 for k in range(0,n)]  # начальное приближение корней

        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = config.maxiter  # максимально допустимое число итераций
        while (I_D.itmarkget() < MAX_ITER):
            #x_prev = copy.deepcopy(x)
            I_D.x_old = copy.deepcopy(x)

            for k in range(0, n):
                S = 0
                for j in range(0, n):
                    if (j != k): S = S + matrix[k,j] * x[j]
                #x[k] = fvec[k] / matrix[k,k] - S / matrix[k,k]
                I_D.x_new[k] = fvec[k] / matrix[k, k] - S / matrix[k, k]
            if isNeedToComplete(I_D.x_new, I_D.x_old):  # проверка на выход
                break
            numberOfIter += 1
            I_D.state_version(numberOfIter)

        print('Количество итераций на решение: ', I_D.itmarkget())

        return I_D.x_new
