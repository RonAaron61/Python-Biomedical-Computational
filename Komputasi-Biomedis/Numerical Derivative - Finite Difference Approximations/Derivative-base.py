#Chapter 8 tugas 2
import numpy as np
import math

xo =  1 #Number for the input X on the derivative
h = 0.001

def fungsi (x):
    #Function
    f = x**2 + 2*x + math.sin(x)
    return f

#turunan secara manual untuk mengetahui error
def turunan (x):    #Manual derivative for error check
    f = 2*x + 2 + math.cos(x)
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