import numpy as np
import functools as ft

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

# Kronecker product for lists of vectors (using reduce from functools)
def kprod(vllist):
    return ft.reduce(lambda x, y: np.kron(x, y), vllist)

# base vectors for one qubit
k0 = ket(0,2)
k1 = ket(1,2)

# some basic matrices

# roots of unity
def w(i,k,n=1):
    return np.exp(2*np.pi*1j*i*k/n).round(12)

# quantum Fourier transform
def qft(n):
    return 1/np.sqrt(n)*np.array([[w(i,k,n) for i in range(n)] for k in range(n)])

# Hadamard gate
h = qft(2)

# not gate
s_x = np.asarray([[0,1],[1,0]])

# controlled-not gate
cnot = cop(s_x)
