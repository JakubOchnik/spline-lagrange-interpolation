import math
import copy


def dot_product(A, b):
    m = len(A)
    n = len(A[0])
    result = [0] * n

    for i in range(m):
        for j in range(n):
            result[i] += A[i][j] * b[j]
    return result


def norm(vec):
    el_sum = 0
    for el in vec:
        el_sum += el * el
    return math.sqrt(el_sum)


def vec_subtract(vec_a, vec_b):
    result = copy.deepcopy(vec_a)
    for i in range(len(vec_a)):
        result[i] -= vec_b[i]
    return result


def copyMatrix(mat):
    new_mat = []
    for row in mat:
        new_row = []
        for element in row:
            new_row.append(element)
        new_mat.append(new_row)
    return new_mat


def make_eye(N):
    mat = []
    for i in range(N):
        mat.append([0]*N)
        mat[i][i] = 1
    return mat
