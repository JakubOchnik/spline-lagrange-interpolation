import numpy as np
import copy
import time
import math

from matrix_handling.matrix_essentials import *


def LU_decompose(N, A):
    # utworzenie L i U
    U = copy.deepcopy(A)
    L = make_eye(N)
    for k in range(N-1):
        for j in range(k+1, N):
            L[j][k] = U[j][k]/U[k][k]
            for i in range(k, N):
                U[j][i] = U[j][i] - L[j][k]*U[k][i]

    return L, U


def fwd_substitution(N, L, b):
    y = [0] * N
    for i in range(N):
        val = b[i]
        for j in range(i):
            val -= L[i][j] * y[j]
        y[i] = val/L[i][i]
    return y


def backward_substitution(N, U, y):
    x = [0] * N
    for i in range(N-1, -1, -1):
        val = y[i]
        for j in range(i + 1, N):
            val -= U[i][j] * x[j]
        x[i] = val/U[i][i]
    return x


def solve_LU(N, A_orig, b_orig, print_info=False):
    A = copy.deepcopy(A_orig)
    b = copy.deepcopy(b_orig)
    startTime = time.time()
    L, U = LU_decompose(N, A)

    # Ly = b
    y = fwd_substitution(N, L, b)
    # Ux = y
    x = backward_substitution(N, U, y)
    
    res = norm(vec_subtract(dot_product(A, x), b))
    elapsedTime = time.time() - startTime
    if print_info:
        print("Last norm: " + str(res))
        print("Elapsed time:" + str(elapsedTime))
    return x, elapsedTime
