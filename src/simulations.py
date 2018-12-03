from simulations.Poisson import Poisson
from simulations.Gamma import Gamma
from simulations.BinNegative import BinNegative
from simulations.HyperGeometric import HyperGeometric
import sys


uso = "uso -- simulations.py [Nombre de la distribución] [No. Muestras]"
if len(sys.argv) < 3:
    print(uso)
    sys.exit(-1)
print("Para salir del programa presione Ctrl + c.")
distribucion = sys.argv[1]
noMuestras = int(sys.argv[2])

if(distribucion == "poisson" or distribucion == "Posisson"):
    while(True):
        lmbda = float(input("Inserte el parámetro λ: "))
        if lmbda >= 0:
            break
        print("λ debe de ser mayor a 0.")
    poisson = Poisson(lmbda,noMuestras)
    poisson.presentaMuestras()
    poisson.grafica()
elif(distribucion == "gamma" or distribucion == "Gamma"):
    n = float(input("Inserte el parámetro n: "))
    lmbda = float(input("Inserte el parámetro λ: "))
    gamma = Gamma(n,lmbda,noMuestras)
    gamma.presentaMuestras()
    gamma.grafica()
elif(distribucion == "binNegative" or distribucion == "BinNegative" or 
            distribucion == "BinNeg"):
    while(True):
        n = float(input("Inserte el parámetro n: "))
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
    binNegativa.grafica()
elif(distribucion == "HiperGeo" or distribucion == "HiperGeometrica"):
    Ngood = float(input("Inserte el parámetro N: "))
    m = float(input("Inserte el parámetro m: "))
    n = float(input("Inserte el parámetro n: "))
    hiperGeo = HyperGeometric(Ngood,m,n,noMuestras)
    hiperGeo.presentaMuestras()
    hiperGeo.grafica()