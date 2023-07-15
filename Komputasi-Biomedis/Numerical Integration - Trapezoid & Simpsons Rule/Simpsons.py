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

#Simpson's 1/3
n = 0
ganjil,genap = 0,0
while a < b-h:
    a+=h
    n+=1
    if (n%2 != 0):
        ganjil+=fungsi(a)
    else:
        genap+=fungsi(a)

simpson = (h/3)*(fa+fb+(4*ganjil)+(2*genap))
print("Simpson 1/3:",simpson,"\tdengan error sebesar:",abs(simpson-exact))