# Chapter 5 - Gauss seidel

"""
2a + b -5c = 9
a - 5b - c = 14
7a - b- 3c = 26
"""
import numpy as np

def galat(x, y):
    galat = abs((x - y) / x)
    return galat

a = np.array([[2, 1, -5],
              [1, -5, -1],
              [7, -1, -3]])
b = np.array([9, 14, 26])
n = len(a)  # panjang baris

# Input tebakan awal
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
xlama = np.zeros((n, 1))  # nilai x yang lama
glt = np.zeros((n, 1))  # galat/error
iter = 1
while True:
    rat = 0  # rata-rata dari galat/error
    print("Iterasi ke-{x}".format(x=iter))

    # Iterasi gauss-seidel begin here
    for j in range(0, n):  # Untuk setiap X yang ada
        sem = 0
        for i in range(0, n):
            if i !=j:
                sem += (A[j][i] * x[i])
        ans = (B[j] - sem) / A[j][j]
        xlama[j] = x[j] #menyimpan x yang lama buat nyari galat
        x[j] = ans  #mengganti nilai x menjadi nilai x yang baru

        glt[j] = galat(x[j], xlama[j])
        rat += glt[j]

    for j in range(0, n):
        print("x{x}".format(x=j+1), x[j], ", error:", glt[j])
    iter += 1
    if rat / n < 0.01:
        break
print("============")
print(f"X1: {x[0]}, X2: {x[1]}, x3: {x[2]}")