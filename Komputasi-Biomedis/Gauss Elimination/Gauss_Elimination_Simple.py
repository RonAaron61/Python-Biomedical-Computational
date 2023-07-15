#Chapter 4. Gauss Elimination

"""
a + b + c = 6
a + 2b - c = 2
2a + b + 2c = 10
"""

import numpy as np

a = np.array([[1, 1, 1], [1, 2, -1], [2, 1, 2]])
b = np.array([6, 2, 10])
n = len(b)

#eliminatioon phase - Forward
for k in range(0,n):
    for i in range(k+1,n):
        if a[i,k] != 0.0:
            lam = a[i,k]/a[k,k]
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
            b[i] = b[i] - lam*b[k]

#backward elimination
x = np.zeros((n,1))
x[n-1] = b[n-1]/a[n-1][n-1] #mendapatkan nilai c

for i in range (n-2,-1,-1):
    sum = 0
    for j in range (i+1,n):
        sum += a[i][j]*x[j]
    x[i] = (b[i]-sum)/a[i][i]   #mendapatkan nilai b lalu a dst...

print("a:",round(x[0][0],4)," ,b:",round(x[1][0],4)," ,c:",round(x[2][0],4))