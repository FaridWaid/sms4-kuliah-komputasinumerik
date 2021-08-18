# Mendefinisikan fungsi agar menjadi integral
def f(x):
    return 1/(1 + x**2)

def simpson(a,b,n):
    # mencari nilai h
    h = (b - a) / n
    
    # Mencari jumlah sementara 
    integrasi = f(a) + f(b)
    
    for i in range(1,n):
        k = a + i*h
        
        if i%2 == 0:
            integrasi = integrasi + 2 * f(k)
        else:
            integrasi = integrasi + 4 * f(k)
    
    # mendapatkan nilai akhir perhitungan
    integrasi = integrasi * h/3
    
    return integrasi
    
a = float(input("Masukkan Batas bawah: "))
b = float(input("Masukkan Batas atas: "))
n = int(input("Masukkan Jumlah interval n: "))
hasil = simpson(a, b, n)
print("Hasil Integrasi= %0.6f" % (hasil) )
