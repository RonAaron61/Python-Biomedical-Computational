import numpy as np
import matplotlib.pyplot as plt

def galat(x, y):
    galat = abs((x - y) / x)
    return galat

# metode Jacobi
"""
2a + b -5c = 9
a - 5b - c = 14
7a - b- 3c = 26
"""

a = np.array([[2, 1, -5],
              [1, -5, -1],
              [7, -1, -3]])
b = np.array([9, 14, 26])
n = len(a)  # panjang baris

x = np.zeros((n, 1))
print("Masukan nilai tebakan untuk:")
for i in range(0, n):
    q = "X{x}: ".format(x=i + 1)
    x[i][0] = int(input(q))

# Pengecekan Dominant Diagonal
A = np.zeros((n, n))  # matriks A baru untuk hasil diagonal dominant
B = np.zeros((n, 1))  # untuk yg B
for i in range(0, n):
    sum = 0
    for j in range(0, n):
        sum += a[i][j]
    for j in range(0, n):
        if abs(a[i][j]) > abs(sum - a[i][j]):
            for k in range(0, n):  # pemasukan isi yang baru
                A[j][k] = a[i][k]
                B[j] = b[i]


#main code
sum = np.zeros((n, 1))  # nilai x yang lama
glt = np.zeros((n, 1))  # galat/error
iter = 1

while iter < 16:
    rat = 0  # rata-rata dari galat/error
    print("Iterasi ke-{x}".format(x=iter))
    # Jacobi iteration begin here
    for j in range(0, n):  # For x1 x2 and so on
        sem = 0
        for i in range(0, n):  # untuk Xn semua kolom
            if i != j:  # keculai si x yg dicari
                sem += (A[j][i] * x[i])  # jumlah semua kolom
        sum[j] = (B[j] - sem) / A[j][j]  # rumus jacobi

    for j in range(0, n):
        glt[j] = galat(sum[j], x[j])
        rat += glt[j]  # mencari rata2 dari error
        x[j] = sum[j]  # mengganti nilai tebakan awal dengan hasil yg baru
        print("x{x}".format(x=j + 1), sum[j], ",error:", glt[j])

    iter += 1
    # Jika memenuhi error
    if (rat / n < 0.01):
        break
