from math import sqrt, cos, pi

from numpy import matmul, ones, mat, array


def two_d_dct(args):
    dim = int(args[2])
    matIn=[]
    for i in range(dim):
        lineIn = []
        for j in range(dim):
            print("Please input A[",i,"][",j,"]")
            lineIn.append(int(input()))
        matIn.append(lineIn)
    a = ones((dim, dim))
    b = mat(matIn)
    ##c = matrix([[20, 20, 25, 25], [20, 20, 25, 25], [30, 30, 20, 20], [30, 30, 20, 20]])
    shape = a.shape[1]
    for i in range(dim):
        for j in range(dim):
            if i == 0:
                x = sqrt(1 / shape)
            else:
                x = sqrt(2 / shape)
            a[i][j] = x * cos(pi * (j + 0.5) * i / shape)

    print(a)
    a_t = a.transpose()
    y1 = matmul(a, b)
    y = matmul(y1, a_t)
    print(y)
    '''
    z1 = matmul(a, c)
    z = matmul(z1, a_t)
    print(z)
    '''
