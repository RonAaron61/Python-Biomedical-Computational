import numpy as np
import matplotlib.pyplot as plt

x = np.array([8,17,20,25,31,42,50,59,65,72,80])
y = np.array([100,130,209,276,330,359,420,487,550,645,700])
n = len(x)
sumx = sumy = sumxy = sumx2 =0

for i in range (0,n):
    sumx += x[i]
    sumy += y[i]
    sumxy += x[i]*y[i]
    sumx2 += x[i]**2

M = np.array([[n, sumx],[sumx,sumx2]])
N = np.array([[sumy],[sumxy]])

ab = np.dot(np.linalg.inv(M),N)
print("Persamaan regresi linearnya adalah: ({x})+({y} X)".format(x=round(ab[0,0],5),y=round(ab[1,0],5)))

ybaru = np.zeros(n,float)
for i in range (0,n):
    ybaru[i] = ab[0,0]+(ab[1,0]*x[i])
plt.title("Regresi")
plt.plot(x,y,'bo-')
plt.plot(x,ybaru,'r^--')
plt.show()