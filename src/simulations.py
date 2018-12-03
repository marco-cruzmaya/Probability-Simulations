from simulations.Poisson import Poisson
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


    