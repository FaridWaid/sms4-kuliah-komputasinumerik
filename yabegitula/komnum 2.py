from numpy import *

def f(x):
    y=x**2-4
    return y

a= int(input("masukkan batas 1:"))
b= int(input("masukkan batas 2 :"))
tl= 0.001
n=1
if(f(a)*f(b)<0):
    x =(a + b) / 2
    print('iterasi','\t', '  a','\t','\t','  b','\t','\t','  x','\t','\t','  f(x)','\t','  f(a)','\t',' keterangan')
    while(abs(f(x))>tl):
        if(f(x)<0 and f(a)>0):
            keterangan ='berlawanan tanda'
        elif (f(x)>0 and f(a)<0):
            keterangan = 'berlawanan tanda'
        else:
            keterangan =''
        print ( n,'\t','\t',"%.5f"%a, '\t', "%.5f"%b, '\t', "%.5f"%x, '\t',"%.5f"% f(x), '\t',"%.5f"%f(a), '\t', keterangan )
        
        if (f(x)*f(a)>0):
            a=x
        else :
            b=x
        x= (a+b)/2
        n+=1
    
    print (n,'\t','\t',"%.5f"%a, '\t', "%.5f"%b, '\t', "%.5f"%x, '\t',"%.5f"% f(x), '\t',"%.5f"%f(a), '\t', keterangan)
    print("akar adalah :" , "%.5f"%x, 'dengan f(x) :', "%.5f"%f(x))
else :
    print("batas tidak valid")