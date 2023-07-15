#chapter 9
from math import exp

def fungsi(t):
    f = t**2 + 2*t + 2
    return f

def integral(t):
    f = (1/3)*(t**3) + t**2 + 2*t
    return f

#integral from a to b
a = 0
b = 5
h = 0.00001

fa = fungsi(a)
fb = fungsi(b)
fn = 0

exact = integral(b)-integral(a)
print("exact:\t\t",exact)

#trapezoid
while a < b-h:
    a+=h
    fn += fungsi(a)

hasil = (h/2)*(fa+fb+(2*fn))
print("Trapezoid:\t",hasil,"\tdengan error sebesar:",abs(hasil-exact))