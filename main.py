import numpy as np
import diagmatrix
import progonka
import config
import relax
import iterationdynamics
import jacobi
import coaffarif
n = config.n
fv:np = diagmatrix.fvector(n)
matrix:np = diagmatrix.rdiagmatrix(n)
jacsolution = jacobi.solution(matrix, fv)
print(jacsolution.x_new)
#print(progonka.solution(matrix, fv, n))

