import numpy as np
import sys
import matplotlib.pyplot as plt

"""
function -- presentarMuestras()
@param arregloMuestras: el arreglo con las muestras.
Función para mejorar la representación de cadena del arreglo entrante.
"""
def presentarMuestras(arregloMuestras):
    n = len(arregloMuestras) #longitud del arreglo
    s = "[ "
    j = 0
    if n == 0:
        return s + "]"
    for i in range(0,n):
        if i == n-1:
            s = s + str(arregloMuestras[i]) + " ]"
        else:
            if j == 15:
                s = s + str(arregloMuestras[i]) + ", \n  "
                j = 0
            else:
                s = s + str(arregloMuestras[i]) + ", "
                j += 1
    return s

"""
function -- grafica()
@param arregloMuestras: el arreglo con las muestras.
Función para graficar las muestras, haciendo uso del módulo matplotlib de python.
"""
def graficar(arregloMuestras):
    plt.hist(arregloMuestras)
    plt.show()


uso = "uso -- python3 simulacionPoisson [λ] [No. Muestras]"
if (len(sys.argv) <= 1):
    print(uso)
    sys.exit(-1)

lambDa = float(sys.argv[1]) #parámetro lambda
noMuestras = int(sys.argv[2]) #número de muestras.
areglo_RandomNum = np.random.poisson(lambDa,noMuestras) #Creación de los números aleatorios de la distribución poisson.
print(presentarMuestras(areglo_RandomNum)) #Se muestran en la pantalla el arreglo de números aleatorios.
graficar(areglo_RandomNum)
