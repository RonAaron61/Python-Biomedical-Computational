#Chapter 3 Newton Raphson
import math

def fungsi(x):  #Fungsi
    #Fx = (3383 +39.9*Y - 0.78*(Y**2) + 0.0039*(Y**3)) - 3850
    Fx = (math.exp(9.214 - (1049.8/(1.985(32+1.6*x))))) - 0.298
    #Fx = (x**2)-x-2
    return Fx

def fungsi2(Y): #Turunan dari fungsi diatas
    Fx = 39.9 - 1.56*Y + 0.0117*(Y**2)
    #Fx = 2*Y-1
    return Fx

#perhitungan
a = float(input("masukan tebakan awal: "))

iterasi = 0
print("Iter|\tX\t\t\t\t\t| F(x)")
while True:
    xn = (a - ((fungsi(a))/fungsi2(a)))
    iterasi += 1
    print(iterasi,"\t",xn,"\t",fungsi(xn))
    if (abs(fungsi(xn)) < 0.01):    #jika sudah memenuhi syarat toleransi
        print("\nNilai akar\t: ",xn)
        print("Dengan error: ",abs(fungsi(xn)))
        break
    else:
        a = xn