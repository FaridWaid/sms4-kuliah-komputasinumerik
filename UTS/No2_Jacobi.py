# pers1 : x1 + 2x2 + 3x3 = 10
# pers2 : 2x1 + 3x2 + 3x3 = 13
# pers2 : x1 + x2 + x3 = 5

def pers1(x2,x3):
    return (10 - 2*x2 - 3*x3)

def pers2(x1,x3):
    return ((13 - (2.0*x1) - (3.0*x3))/3)

def pers3(x1,x2):
    return (5 - x1 - x2)

def error(n,o):
    return ((n-o)/n) * 100

itMax = 5
current = [0,0,0]
er=[]
akhir = [0,0,0]
for i in range(itMax+1):
   er[0:3] = current[0:3]
   if i == 0:
       print("Iterasi-",i," =", akhir)
   else:
       current.clear()
       current.append(eval("{0:.3f}".format(pers1(akhir[1],akhir[2]))))
       current.append(eval("{0:.3f}".format(pers2(akhir[0],akhir[2]))))
       current.append(eval("{0:.3f}".format(pers3(akhir[0],akhir[1]))))
       akhir[0:3] = current[0:3]
       print("Iterasi- ",i," =", akhir)
print("Error = [", "{0:.2f},".format(error(akhir[0], er[0])), "{0:.2f},".format(error(akhir[1],er[1])), "{0:.2f}".format(error(akhir[2],er[2])),"]")

