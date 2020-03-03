import numpy as np

# ket vectors 
def ket(x,d):
    ret = np.zeros(d,dtype=np.int8)
    ret[x] = 1
    return np.asarray([ret])

# projector
def proj(x):
    return np.kron(np.asarray(x).T, np.asarray(x))

# identity matrix
def I(d):
    return np.identity(d)

# controlled operations
def cop(x):
    s = x.shape[0]
    return np.kron(proj(ket(0,s)),I(s)) + np.kron(I(s)-proj(ket(0,s)), x)

# base vectors for one qubit
k0 = ket(0,2)
k1 = ket(1,2)

# some basic matrices

# not gate
s_x = np.asarray([[0,1],[1,0]])

# controlled-not gate
cnot = cop(s_x)
