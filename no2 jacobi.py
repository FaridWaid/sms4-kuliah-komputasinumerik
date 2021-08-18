import numpy

def jacobi(A, xzero):
    baris = numpy.size(A, 0)
    xi = []
    xkira = []
    xminus = xzero[:]
    for j in range(baris):
        xi = (A[j, :]/A[j][j])
        sumel = xi[baris]
        for k in range(baris):
            if k == j: continue
            sumel = sumel - (xi[k] * xzero[k])
        xkira.append(sumel)
    xzero = xkira
    delta = numpy.subtract(xzero, xminus)
    ea = abs(numpy.divide(delta, xzero) * 100)
    return [xzero, ea]

matrix1 = numpy.array([[1.,2.,3.,10], [2.,3.,3.,13], [1.,1.,1.,5]]) 
xzero = [0,0,0]
print (jacobi(matrix1,xzero))