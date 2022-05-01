import numpy as np
import diagmatrix
import progonka
import config
import relax
import accurancy
import jacobi
import coaffarif
n = config.n
fv:np = diagmatrix.fvector(n)
matrix:np = diagmatrix.rdiagmatrix(n)
print(progonka.solution(matrix, fv, n))

