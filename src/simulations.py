from simulations.Poisson import Poisson
from simulations.Gamma import Gamma
from simulations.BinNegative import BinNegative
from simulations.HyperGeometric import HyperGeometric
import sys
import math


def size(muestras):
    size = 0
    n = len(muestras)
    for i in range(0,n):
        size = size + muestras[i]
    return size/n

uso = "uso -- simulations.py [Nombre de la distribución] [No. Muestras]"
if len(sys.argv) < 3:
    print(uso)
    sys.exit(-1)
print("Para salir del programa presione Ctrl + c.")
distribucion = sys.argv[1]
noMuestras = int(sys.argv[2])

if(distribucion == "poisson" or distribucion == "Poisson"):
    while(True):
        lmbda = float(input("Inserte el parámetro λ: "))
        if lmbda >= 0:
            break
        print("λ debe de ser mayor a 0.")
    poisson = Poisson(lmbda,noMuestras)
    poisson.presentaMuestras()
    print("  Media de la muestra: %.4f" % size(poisson.muestras))
    poisson.grafica()
elif(distribucion == "gamma" or distribucion == "Gamma"):
    while(True):
        n = float(input("Inserte el parámetro n: "))
        n = math.floor(n)
        if n > 0:
            break
        print("n debe de ser mayor a 0.")
    while(True):
        lmbda = float(input("Inserte el parámetro λ: "))
        if lmbda >= 0:
            break
        print("λ debe de ser mayor a 0.")
    gamma = Gamma(n,lmbda,noMuestras)
    gamma.presentaMuestras()
    print("  Media de la muestra: %.4f" % size(gamma.muestras))
    gamma.grafica()
elif(distribucion == "binNegative" or distribucion == "BinNegative" or 
            distribucion == "BinNeg"):
    while(True):
        n = int(input("Inserte el parámetro n: "))
        if n >= 0:
            break
        print("n debe de ser mayor o igual a 0.")
    while(True):
        p = float(input("Inserte el parámetro p: "))
        if p <= 1 and p >= 0:
            break
        print("p debe de ser menor o igual a 1 o mayor o igual a 0.")
    binNegativa = BinNegative(n,p,noMuestras)
    binNegativa.presentaMuestras()
    print("  Media de la muestra: %.4f" % size(binNegativa.muestras))
    binNegativa.grafica()
elif(distribucion == "HiperGeo" or distribucion == "HiperGeometrica"):
    n = int(input("Inserte el parámetro de tamaño de la muestra: "))
    N = int(input("Inserte el parámetro N: "))
    m = int(input("Inserte el parámetro m: "))
    hiperGeo = HyperGeometric(n,N,m,noMuestras)
    hiperGeo.presentaMuestras()
    print("  Media de la muestra: %.4f" % size(hiperGeo.muestras))
    hiperGeo.grafica()