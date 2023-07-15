import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,5,7,10,12,13,16,18,20])
y = np.array([3,2,6,5,8,7,10,8,12,10])

n = len(x)
sumx=0
sumy=0
sumxy=0
sumx2y=0
sumx2=0
sumx3=0
sumx4=0

for i in range(0,n):
    sumx+=x[i]
    sumy += y[i]
    sumxy += x[i]*y[i]
    sumx2 += x[i]**2
    sumx3 += x[i]**3
    sumx4 += x[i]**4
    sumx2y += (x[i]**2)*y[i]

M = np.array([[n, sumx, sumx2],[sumx,sumx2,sumx3],[sumx2,sumx3,sumx4]])
N = np.array([[sumy],[sumxy],[sumx2y]])

ab = np.dot(np.linalg.inv(M),N)
print("Persamaan regresi linearnya adalah: ({a})x2 + ({b})x + ({c})".format(a=round(ab[2,0],3),b=round(ab[1,0],3), c=round(ab[0,0],3)))

ybaru = np.zeros(n)
for i in range (0,n):
    ybaru[i] = ab[2]*x[i]**2+ab[1]*x[i]+ab[0]

plt.plot(x,y,'bo--')
plt.plot(x,ybaru,'r^-')
plt.show()