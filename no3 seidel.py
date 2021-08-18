import numpy

def seidel(A, xzero):
    baris = numpy.size(A, 0)
    xi = []
    xminus = xzero[:]
    for j in range(baris):
        xi = (A[j, :]/A[j][j])
        sumel = xi[baris]
        for k in range(baris):
            if k == j: continue
            sumel = sumel - (xi[k] * xzero[k])
        xzero[j] = sumel
    delta = numpy.subtract(xzero, xminus)
    ea = abs(numpy.divide(delta, xzero) * 100)
    return [xzero, ea]

matrix1 = numpy.array([[10.,-1.,2.,0.,6.,10.,-1.,2.,0.,6.,55], [-1.,11.,-1.,3.,2.,-1.,-11.,-1.,3.,2.,55], [-1.,11.,-1.,3.,2.,-1.,-11.,-1.,3.,2.,55], [-1.,11.,-1.,3.,2.,-1.,-11.,-1.,3.,2.,55],
                        [10.,-1.,2.,0.,6.,10.,-1.,2.,0.,6.,55], [-1.,11.,-1.,3.,2.,-1.,-11.,-1.,3.,2.,55], [10.,-1.,2.,0.,6.,10.,-1.,2.,0.,6.,55], [10.,-1.,2.,0.,6.,10.,-1.,2.,0.,6.,55],
                        [10.,-1.,2.,0.,6.,10.,-1.,2.,0.,6.,55], [-1.,11.,-1.,3.,2.,-1.,-11.,-1.,3.,2.,55]]) 
xzero = [0,0,0,0,0,0,0,0,0,0]
print (seidel(matrix1,xzero))