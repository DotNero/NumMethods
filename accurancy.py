import numpy as np
import config
import math
def accuracyparametr(xi, fi):
    return(math.abs(xi-fi))
def accuracyparametrforvector(xvector:np, fvector:np):
    rvector = np.zeros((n))
    for i in range(config.n):
        rvector[i] = accuracyparametr(xvector[i],fvector[i])
        return(rvector)


