import numpy as np
import config
import math
n = config.n
def accuracyparametr(xi, fi, matrixi ):
    return(math.fabs(xi-fi))
def maxvectoraccuracy(xvector:np, fvector:np, matrix:np):
    prev = np.dot(matrix, xvector)
    res = np.abs(prev - fvector)
    max = np.max(res)
    return(max)


