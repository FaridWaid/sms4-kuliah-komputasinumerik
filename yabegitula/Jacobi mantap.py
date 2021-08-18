def x1(x2,x3):
    return (10 - 2*x2 - 3*x3)

def x2(x1,x3):
    return ((13 - (2.0*x1) - (3.0*x3))/3)

def x3(x1,x2):
    return (5 - x1 - x2)

def error(n,o):
    return ((n-o)/n) * 100

#Nilai Awal
bx1, bx2, bx3 = 0,0,0

tabel = "{0:1} | {1:7} | {2:7} | {3:7} | {4:7} | {5:7} | {6:7}"
print(tabel.format("i", "X1", "X2", "X3", "E1", "E2", "E3"))
for i in range(0,6):
    if i == 0:
        print(tabel.format(i, bx1, bx2, bx3, "-", "-", "-"))
        cx1 = bx1
        cx2 = bx2
        cx3 = bx3
    else:
        cx1 = eval("{0:.3f}".format(x1(bx2,bx3)))
        cx2 = eval("{0:.3f}".format(x2(bx1,bx3)))
        cx3 = eval("{0:.3f}".format(x3(bx1,bx2)))
        print(cx1)
        print(bx1)
        print(tabel.format(i, cx1, cx2, cx3, "{0:.2f}".format(error(cx1, bx1)), "{0:.2f}".format(error(cx2,bx2)), "{0:.2f}".format(error(cx3,bx3))))
        
    bx1 = cx1
    bx2 = cx2
    bx3 = cx3
