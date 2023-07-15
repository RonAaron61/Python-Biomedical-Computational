#Chapter 8 tugas 2
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array([1.2, 1.4, 1.6, 1.8])
y = np.array([0.8333, 0.7143, 0.6250, 0.5556])

n = len(y)
hasil = np.poly1d([0])

for i in range (0,n):
    atas = np.poly1d([1])
    bawah = 1
    for j in range (0,n):
        if i!=j:
            atas *= np.poly1d([1,-x[j]])
            bawah *= (x[i]-x[j])
    hasil += (y[i]*(atas/bawah))

print ("Persamaan:\n",hasil,"\n")

xo =  1.5
h = 0.0001
def fungsi (x):
    return hasil(x)

#turunan secara manual untuk mengetahui error
def turunan (x):
    f = -0.6126*(x**2) + 2.458*x - 2.752
    return f
exact = turunan(xo)


#Forward
forward = (fungsi(xo+h) - fungsi(xo))/h
#backward
backward = (fungsi(xo)-fungsi(xo-h))/h
#center
center = (fungsi(xo+h)-fungsi(xo-h))/(2*h)

print("Exact:", exact)
print("Forward:", forward,"\tError:",(forward-exact))
print("Backward:", backward,"\tError:",(backward-exact))
print("Center:", center,"\tError:",(center-exact))

"""
def fungsi (x):
    return x*math.sin(x)
def turunan (x):
    return x*math.cos(x) + math.sin(x)
xo = 1
h = 10**(-15)
exact = turunan(xo)
n = 15
fwd,bck,cnt = [],[],[]
xname = []
while h <= 1:
    forward = (fungsi(xo+h) - fungsi(xo))/h
    backward = (fungsi(xo)-fungsi(xo-h))/h
    center = (fungsi(xo+h)-fungsi(xo-h))/(2*h)

    kata = "10e-{x}".format(x = n)
    n -= 1
    xname.append(kata)

    fwd.append(forward-exact)
    bck.append(backward-exact)
    cnt.append(center-exact)

    h+= (h*10)

plt.plot(xname,fwd,'r-',label='forward')
plt.plot(xname,bck,'g-',label='backward')
plt.plot(xname,cnt,'y-',label='center')
plt.legend()
plt.show()
"""