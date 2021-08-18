import numpy as np
#Iold = Integral f(x) dari x = a to b dihitung berdasarkan trapezoidal rule dengan 2^(k-1) panels.
def trapezoid(f,a,b,Iold,k):
    if k == 1:Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k -2 )      # Number of new points
        h = (b - a)/n       # Spacing of new points
        X = a + h/2.0       # Coord. of 1st new point
        sum = 0.0
        for i in range(n):
            sum = sum + f(X)
            x = x + h
        Inew = (Iold + h*sum)/2.0
    return Inew

a = 0
b = 90
k = 3
Iold = 0
x = np.linspace(a,b,k)
f = np.sin(x)
print(trapezoid(f,a,b,Iold,k))