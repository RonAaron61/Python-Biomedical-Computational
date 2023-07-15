#Chapter 13 no 1 Runge-Kutta Orde 4
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

#untuk plot
xi = [x]
yi = [y]
ex = [exact(x)]
tb = PrettyTable(["t","y","exact","error"])
tb.add_row([round(x, 3), y, exact(x), (abs(exact(x) - y))])

while a <= b:
    k1 = h*fungsi(y)
    k2 = h*fungsi(y+ (1/2)*k1)
    k3 = h*fungsi(y+ (1/2)*k2)
    k4 = h*fungsi(y+k3)
    y += (1/6)*(k1+ (2*k2)+(2*k3)+k4)
    x += h
    a = round((a+h),3)

    tb.add_row([round(x, 3), y, exact(x), (abs(exact(x) - y))])
    
    #plot
    xi.append(x)
    yi.append(y)
    ex.append(exact(x))

print(tb)
plt.title("Tugas 1 - Orde 4 Runge-kutta's")
plt.legend(["Runge-Kuttas's",'exact'])
plt.xlabel("Waktu (t)")
plt.ylabel("Muatan (q)")
plt.plot(xi,yi,'b--')
plt.plot(xi,ex,'r-')
plt.show()