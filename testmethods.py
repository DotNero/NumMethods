import numpy as np
import diagmatrix
#метод прогонки устойчив при обладании матрицы свойством диагонального преобладания
def diagtest(matrix:np):
    for i, j in range(np.shape(matrix)):
        if matrix[i,i] <= matrix[i,j]:
            if i != j:
                return(False)
    return(True)
