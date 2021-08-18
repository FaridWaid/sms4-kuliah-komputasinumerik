f=inline('4*x-x^2','x');
hasil_eksak=1.6667;
a=input('masukkan batas bawah integrasi :');
b=input(' masukkan batas atas integrasi :');
N=input('masukkan jumlah segmen N :');
h=(b-a)/N;
sum=f(a)+f(b);
fak=2
for i=1:
    N-1
    x=a+i*h;
    sum=sum+2*f(x)
end
hasil_numerik=sum*h/2.;
selisih=hasil_eksak-hasil_numerik;
kesalahan=abs(selisih/hasil_eksak);
fprintf('%f %f',hasil_numerik,kesalahan);

#from math import sin, pi

#bawah = 0
#atas = pi/2
#n = 1
#h = ((atas-bawah)/ (2**n))
#f = lambda x: sin(x)

#def trapezoid (bawah, atas, f, h, n):
#    S = 0.5 * (f(bawah) + f(atas))
#    for i in range(0,n+1):
#        x = bawah + i*h
#        S+= f(x)
 #   totalS = h * S
  #  return totalS


#print(trapezoid(bawah,atas,f,h,n))

