from numpy import array, zeros
import numpy as np
#~~~~~~inisialisasi matrik augment~~~~~#
jumlah = int(input("Masukkan Jumlah Persamaan: "))
persamaan = np.zeros((jumlah,jumlah+1))

for i in range(jumlah):
    for j in range(jumlah+1):
        if j == (jumlah):
            persamaan[i][j] = float(input( 'Hasil persamaan ' + str(i+1) + ' = '))
        else:
            persamaan[i][j] = float(input( 'a['+str(i)+']['+ str(j)+'] = '))

print("######### PERSAMAAN LINIEAR #########")
print (persamaan)

#===== METODE ELIMINASI GAUSS =========#
n=len(persamaan)
#~~~~~~proses triangularisasi~~~~~~~~~~#
for k in range(0,n-1):
    #-----proses pivot dari sini----------#
    #Untuk menghindari angka 0 pada pembaggi
    #dan juga untuk menukar persamaan dengan persamaan pada baris dibawahnya
    if persamaan[k,k]==0:
        for s in range(0,n+1):
            v=persamaan[k,s]
            u=persamaan[k+1,s]
            persamaan[k,s]=u
            persamaan[k+1,s]=v
    #-----proses pivot sampai sini----------#
    for i in range(k+1,n):
        faktor=persamaan[i,k]/persamaan[k,k]
        for j in range(0,n+1):
            persamaan[i,j]=persamaan[i,j]-faktor*persamaan[k,j]

#~~~~~~proses substitusi-mundur~~~~~~~~#
X = zeros((n,1))
X[n-1,0]=persamaan[n-1,n]/persamaan[n-1,n-1]
for j in range(n-2,-1,-1):
    S=0
    for i in range(j+1,n):
        S=S+persamaan[j,i]*X[i,0]
        X[j,0]=(persamaan[j,n]-S)/persamaan[j,j]
#======================================#
#Hasil Output
print("######### HASIL OUTPUT #########")
for i in range(0,len(X)):
    print ("X -",(i+1), " = ", int(X[i])) 
