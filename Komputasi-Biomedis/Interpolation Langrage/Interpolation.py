#Chapter 7 tugas 5
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

x = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3])
y = np.array([0.030, 0.067, 0.148, 0.248, 0.320, 0.518, 0.697])
#data tugas 2 diatas

"""
ai1 = np.array([56.6, 53.4, 45.5, 48.4, 45.8, 43.5, 42, 40.3, 35.5, 5.9])
ai2 = np.array([53.8, 52.7, 48.6, 46.4, 46.3, 43, 42, 39.5, 36.5, 9.3])
ai3 = np.array([54.3, 52.1, 48.2, 46.6, 46.1, 43.4, 41.1, 41.3, 35.3, 11.7])
ai4 = np.array([53.6, 51.1, 47.9, 45.8, 44.8, 43.2, 42.8, 38.7, 39, 7.7])

y = np.array([st.mean(ai1), st.mean(ai2), st.mean(ai3), st.mean(ai4)])
x = np.array([0.5, 1.0, 1.5, 2.0])
"""
n = len(y)
hasil = np.poly1d([0])

for i in range (0,n):
    atas = np.poly1d([1])
    bawah = 1
    for j in range (0,n):
        if i!=j:
            atas *= np.poly1d([1,-x[j]])
            bawah *= (x[i]-x[j])
    hasil += (y[i]*(atas/bawah))

print (hasil)
#x_prediksi = np.array([0.365, 0.512, 0.621, 0.715]) - tugas 2
#x1 = np.arange(min(x_prediksi)-0.1, max(x_prediksi)+0.1, 0.001) - tugas 2
x1 =np.arange(min(x)-0.1, max(x)+0.1, 0.01)
y1 = hasil(x1)
plt.title("Interpolasi")
plt.plot(x1,y1,'b-')
#plt.plot(x_prediksi,hasil(x_prediksi),'ro-') - tugas 2
plt.plot(x,y,'ro-')
plt.show()