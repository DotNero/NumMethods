

#этот метод служит для создания диагональной матрицы нужного размера
#подойдёт и для создания трёхдиагональной матрицы
import numpy as np
from scipy.sparse import dia_matrix
import coaffarif
import config

n:int = config.n
h = 1/n
def nptop(n):
    top = np.zeros((n))
    for i in range(n):
        top[i] = -(coaffarif.ai(i,h))
    return(top)
def npmiddle(n):
    middle = np.zeros((n))
    for i in range(n):
        middle[i] = coaffarif.ai(i,h) + coaffarif.ai(i+1,h) + h**2*coaffarif.gi(i,h)
    return(middle)
def npbottom(n):
    bottom = np.zeros((n))
    for i in range(n):
        bottom[i] = -coaffarif.ai(i+1,h)
    return(bottom)
def matrixofdiagonals(n):
    #vstack - объединяет матрицы вертикально
    return(np.vstack((npmiddle(n),npbottom(n),nptop(n))))
def fvector(n):
    fvec = np.zeros((n))
    for i in range(n):
        fvec[i] = coaffarif.f(i,h)*(h*h)
    return(fvec)
def rdiagmatrix(n):
    matrixx = dia_matrix((matrixofdiagonals(n), [0, -1, 1]),shape=(n, n)).toarray()
    return(matrixx)
#def(alpha, betta, gamma ):
#def(np.top, np.middle,np.bot):
print(matrixofdiagonals(n))
#matrix = dia_matrix((np.array([[13, 14, 15, 28, 33], [15, 16, 18, 22, 32], [17, 18, 19, 44, 71]]), [0, -1, 1]),
#            shape=(n, n)).toarray()

#это должно работать!!!