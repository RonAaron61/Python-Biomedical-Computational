#Chapter 4. Gauss Elimination
import numpy as np
import matplotlib.pyplot as plt

#Output untuk R dan hasil x
for i in range(60,95,5):    #range tidak bisa float
    r = i/100
    # x1 = lung
    # x2 = liver
    a = np.array([[(1.5 * r) - 3.2366, 0.5 * r],
                  [0.5, -18.409333]])
    b = np.array([-0.7, -2.8175])
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
    x[n-1] = b[n-1]/a[n-1][n-1] #mendapatkan nilai x2 (x[1])/(liver)
    for i in range (n-2,-1,-1):
        sum = 0
        for j in range (i+1,n):
            sum += a[i][j]*x[j]
        x[i] = (b[i]-sum)/a[i][i]   #mendapatkan nilai x1 (lung)

    print("Untuk R:", r)
    print("x1:",round(x[0][0],4),",x2:",round(x[1][0],4))
    print("---------------------\n")

    #plot grafik napthalene epoxide concentrations at
    #Lung - x1
    plt.subplot(211)
    plt.title("Lung")
    plt.ylabel("NO concentrations")
    plt.xlabel("Recycle fraction")
    plt.plot(r,x[0][0],'bo-')
    #Liver - x2
    plt.subplot(212)
    plt.title("Liver")
    plt.ylabel("NO concentrations")
    plt.xlabel("Recycle fraction")
    plt.plot(r,x[1][0],'ro-')

plt.show()