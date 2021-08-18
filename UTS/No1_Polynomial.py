x=[1.0,2.0,3.0,4.0,5.0,6.0]
y=[14.5,19.5,30.5,53.5,94.5,159.5]

n=len(y)
matrix=[0]*n
hasil=[]
for i in range (n):
    matrix[i]=[0]*n

for i in range (n):
    matrix[0][i]=y[i]

for i in range (1,n,1):
    for j in range (1,n-(i-1),1):
        matrix[i][j-1]=(matrix[i-1][j]-matrix[i-1][j-1])/(x[i+j-1]-x[0+j-1])
        
print (matrix)
for i in range (n):
    hasil.append(matrix[i][0])
print ("hasil = ",hasil)
X=int(input("silakan input nilai x untuk fungsi f(x). x = "))
d0 = hasil[0]
d1 = hasil[1]*(X-x[0])
d2 = hasil[2]*(X-x[0])*(X-x[1])*(X-x[2])
d3 = hasil[3]*(X-x[0])*(X-x[1])*(X-x[2])*(X-x[3])
d4 = hasil[4]*(X-x[0])*(X-x[1])*(X-x[2])*(X-x[3])*(X-x[4])
d5 = hasil[5]*(X-x[0])*(X-x[1])*(X-x[2])*(X-x[3])*(X-x[4])*(X-x[5])
print ("hasil newton= f(",X,") = ",d0+d1+d2+d3+d4+d5)
