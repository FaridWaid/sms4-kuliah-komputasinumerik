import numpy as np

def jacobi(A,b,init):
    itmax=7
    tolmax=1e-15
    A=np.matrix(A)
    b=np.matrix(b).T
    N=np.diag(np.diag(A))
    Ni=np.linalg.inv(N)
    P = A-N
    xo=np.matrix(init).T
    for i in range(itmax):
        xn=Ni*b-Ni*P*xo
        xo=xn
        eror=b-A*xo
        normEror=np.linalg.norm(eror)
        if normEror<tolmax:
            break
    return i,np.array(xo).flatten(), normEror


A =[[1,2,3],[2,3,3],[1,1,1]]
b= [10,13,5]
initA=[0,0,0]
solA=jacobi(A,b,initA)
print(solA)

