from math import factorial, exp, cos

def exponensial (x, n):
    hasil = 0.0
    for i in range (0, n): # menjalankan sebanyak faktor mulai 0 sampai n-1 (n faktor)
        hasil = hasil + x**i/factorial(i)
    return hasil

oldval = 0.0 # inisialisasi nilai awal
x = 1
n = 1
trueval = exp (x)-cos(x)
print ("nilai asli :","%.8f"%trueval)
print('faktor','\t','estimasi','\t','true error','\t','error relatif')
ca =1
while(ca>0.001):
    val = exponensial (x, n)-cos(x)
    ct = abs((val-trueval)/trueval)*100
    ca = abs((val-oldval)/val)*100
    oldval = val
    
    print (n ,'\t',"%.8f"%val,'\t',"%.8f"%ct,'\t',"%.8f"%ca)
    n+=1
print ("nilai yang mendekati :", "%.8f"%val,"dengan error","%.8f"%ct)