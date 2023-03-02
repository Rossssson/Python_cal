import numpy as np

if __name__=='__main__':
    a = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 2], [1, 1, 1, 1], [2, 2, 2, 4], [1, 2, 4, 4], [1, 2, 1, 2], [2, 3, 3, 3],
         [4, 4, 4, 4]]
    x=np.zeros((4,1))
    cov=np.zeros((4,4))
    for ele in a:
        ele = np.mat(ele)
        ele = np.transpose(ele)
        x+=ele
    x=1/9*x
    for vec in a:
        vec = np.mat(vec)
        vec = np.transpose(vec)
        res = np.matmul((x-vec),(np.transpose(x-vec)))
        cov+=res
    cov = cov*1/8
    print(cov)

    m,n = np.linalg.eig(cov)
    print("value: ",m)
    print("vector: ",n)


