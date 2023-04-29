import numpy as np


def diagonanlize(T,n):
    if T is None:
        return []

    eValues, eVectors = np.linalg.eig(T)
    C = eVectors
    C_inv = np.linalg.inv(C)
    D = np.diag(T)
    D_pow_n = matrix_pow(T, n)

    """
    T = CD^nC^-1
    """
    return (C @ D_pow_n) @ C_inv

def matrix_pow(matrix,n):
    if matrix is None:
        return []

    X = matrix
    for i in range(0,n):
        X = np.matmul(X,matrix)
    
    return X