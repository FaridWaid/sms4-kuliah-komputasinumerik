import numpy as np

k = 100

a = np.array([[1., 2., 3.],
              [2., 3., 3.],
              [1., 1., 1.]])
b = np.array([10., 13., 5.])

print("system:")
for i in range(a.shape[0]):
    row = ["{}*x{}".format(a[i, j],j+1)for j in range(a.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for it_count in range(k):
    print ("current solution =",x)
    x_new = np.zeros_like(x)

    for i in range(a.shape[0]):
        s1 = np.dot(a[i, :i], x[:i])
        s2 = np.dot(a[i, i+1:], x[i+1:])
        x_new[i] = (b[i] - s1 - s2)/a[i, i]

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x=x_new

print("solution:")
print(x)
error= np.dot(a, x) - b
#print("error:")
#print (error)
