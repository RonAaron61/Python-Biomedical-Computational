#chapter 11
import math
import numpy

def fungsi(x):
    f = x**2 + 2*x + 2
    return f

def integral (x):
    f = (1/3)*(x**3) + x**2 + 2*x
    return f

#trapezoid
def trapezoid (h):
    global a,b
    A,B = a,b
    fn = 0
    while A < B-h:
        A+=h
        fn += fungsi(A)
    fa = fungsi(a)
    fb = fungsi(b)
    return ((h/2)*(fa+fb+(2*fn)))

#Richardson
def richardson(h):
    Ih = trapezoid(h)
    I2h = trapezoid((2*h))
    #trap = (I2h + ((I2h-Ih)/((2**2)-1)))
    trap = (Ih + ((Ih-I2h)/((2**2)-1)))
    return trap


a = 0
b = 5
k = 3

arr = numpy.zeros([k+1,k+1])
#Hasil untuk A0 - Ak (Menggunakan Trapezoid)
for i in range (0,k+1):
    n = 2 ** i
    h = (b - a)/n
    #arr[i][0] = trapezoid(h)
    arr[i][0] = richardson(h)

#Romberg
q = 0
for i in range (1,k+1):
    q += 2
    for j in range (i,k+1):
        arr[j][i] = (arr[j][i-1] + ((arr[j][i-1]-arr[j-1][i-1])/((2**q)-1)))
print(arr,"\n")

exact = (integral(b)-integral(a))

print("exact\t:",exact)
print("Romberg\t:", arr[k][k], "Error:", abs(exact-arr[k][k]))
print("trap\t:", trapezoid(0.001), "Error:", abs(exact-trapezoid(0.001)))