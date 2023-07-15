#tugas chapter 10
import math

def fungsi (x):
    return math.exp(x)

def integral (x):
    return math.exp(x)

h = 0.001
xo = 1.2


D2h = (fungsi(xo+(2*h))-fungsi(xo-(2*h)))/(2*(2*h))
D4h = (fungsi(xo+(4*h))-fungsi(xo-(4*h)))/(2*(4*h))

"""Metode Lain"""
forward = (fungsi(xo+h) - fungsi(xo))/h
backward = (fungsi(xo)-fungsi(xo-h))/h
center = (fungsi(xo+h)-fungsi(xo-h))/(2*h)

n = 4   #ordo error

F = D2h + ((D2h - D4h)/((2**n)-1))  #Rumus ekstrapolasi
exact = (integral(xo))              #exact
error = abs(F-exact)                #error

print("Exact :\t", exact)
#print("D(h) :\t",Dh,"\terror:",abs(Dh-exact))
print("D(2h) :\t",D2h, "\t,error:",abs(D2h-exact))
print("D(4h) :\t",D4h, "\t,error:",abs(D4h-exact))
print("Ekstrapolasi:",F, "error:",error)
print("\nOther Method for comparison")
print("Forward:\t", forward, "error:",abs(forward-exact))
print("Backward:\t", backward, "error:",abs(backward-exact))
print("Center:\t\t", center, "error:",abs(center-exact))