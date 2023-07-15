#Chapte 12 - Euler
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def fungsi (y):
    f = (12/(8*(10**(5))))-(y/((8*(10**5))*(5*(10**(-6)))))
    return f

def exact (t):
    f = (5*(10**(-6)))*12*(1-math.exp((-t)/((8*(10**5))*(5*(10**(-6))))))
    return f

a,b = 0,2
x = 0.0   #t0
y = 0.0   #q
h = 0.1
xi = [x]
yi = [y]
ex = [exact(x)]
tb = PrettyTable(["t","y","exact","error"])

#Heun method
while a <= b:
    #print (x,y,exact(x))
    xi.append(x)
    yi.append(y)
    ex.append(exact(x))
    tb.add_row([ round(x,3), y, exact(x), (abs(exact(x) - y))])
    yp = y + (h * fungsi(y))
    y = y + (h/2)*(fungsi(y)+fungsi(yp))
    x += h
    a = round((a+h),3)

print(tb)
plt.title("Tugas 1 - Heun")
plt.legend(['Heun','exact'])
plt.xlabel("Waktu (t)")
plt.ylabel("Muatan (q)")
plt.plot(xi,yi,'b--')
plt.plot(xi,ex,'r-')
plt.show()