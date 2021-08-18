def romberg(f,a,b,n):
hasil=[]
h = (b−a)
hasil.append([(h/2.0)∗(f(a)+f(b))])
for i in range(1,n+1):
    h = h/2.
    sum = 0
    for k in range(1,2∗∗i ,2):
        sum = sum + f(a+k∗h)

        hasilSementara = [0.5∗hasil[ i−1][0] + sum∗h]
        for j in range(1,i+1):
        rij = hasilSementara[j−1] + (hasilSementara[j−1]−hasil[i−1][j−1])/(4.∗∗j−1.)
        hasilSementara.append(rij)
    hasil.append(hasilSementara)

return hasil
