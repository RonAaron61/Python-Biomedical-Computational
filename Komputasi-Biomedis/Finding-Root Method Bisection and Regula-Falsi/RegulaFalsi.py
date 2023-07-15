#tugas Regula Falsi
import math
awal = float(input("masukan range awal: "))
akhir = float(input("masukan range akhir: "))

#mencari nilai tengah
def tengah(a,b):
    Fx = ((a * (fungsi(b))) - (b * (fungsi(a)))) / (fungsi(b) - fungsi(a))
    return Fx

#mencari nilai fungsi
def fungsi(x):
    #Fx = x - (2*math.cos(math.radians(x))) #Tugas pendahuluan
    Fx = ((150*((((1-x)**2)*0.01*0.75)/0.1**2)+(1.75*(((1-x)**2)*1*(0.75**2))/0.1))-(810.5/20))
    return Fx

#perhitungan
def perhitungan(a,b):
    i=a             #menyimpan nilai awal untuk di output
    j=b             #menyimpan nilai akhir untuk di output
    iterasi = 0     #menyimpan jumlah iterasi yg dilakukan
    #looping mencari akar
    while True:
        X = fungsi(a)
        Y = fungsi(b)
        #persyaratan awal
        if X*Y < 0:
            Z = tengah(a,b)
            iterasi += 1
            #seleksi a dan b selanjutnya!
            if (fungsi(Z)<0) == (X<0): #jika range diantara a dan z:
                #dengan asumsi nilai Z pasti yg paling kecil/mendekati 0
                if fungsi(Z) > -0.01 and fungsi(Z)<0.01:
                    return result(i,j,Z,iterasi)
                    break
                a = Z   #mengganti nilai a menjadi nilai tengah

            else: #jika range diantara b dan z:
                if fungsi(Z) > -0.01 and fungsi(Z) < 0.01:
                    return result(i,j,Z,iterasi)
                    break
                b = Z   #mengganti nilai b menjadi nilai tengah
        #jika tidak ada akar
        else:
            print("======================================")
            print("*Dengan nilai toleransi 0.01")
            print("untuk range[{0}, {1}], tidak ada akar".format(a,b))
            print("Dengan nilai fungsi:")
            print("F(a): ", fungsi(a))
            print("F(b): ", fungsi(b))
            print("======================================")
            break

def result(a,b,c,iter): #menampilkan result
    print("======================================")
    print("*Dengan nilai toleransi 0.01")
    print("untuk range[{0}, {1}]:".format(a,b))
    print("Dengan iterasi sebanyak {0}x, didapatkan:".format(iter))
    print("x:", c)
    print("Dengan nilai fungsi F(x):", fungsi(c))
    print("======================================")

perhitungan(awal,akhir)