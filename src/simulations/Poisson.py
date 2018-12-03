import numpy as np
import sys
import matplotlib.pyplot as plt


class Poisson:
    def __init__(self, lmbda, noMuestras):
        self.lmbda = lmbda
        self.noMuestras = noMuestras
        self.muestras = self.simula()
    
    """
    Method --simula()
    Método para crear las muestras a simular.
    """
    def simula(self):
        return np.random.poisson(self.lmbda,self.noMuestras)
    """
    Method -- presentaMuestras()
    Método para mejorar la representación de cadena del arreglo de muestras.
    """
    def presentaMuestras(self):
        n = len(self.muestras) #longitud del arreglo
        s = "[ "
        j = 0
        if n == 0:
            return s + "]"
        for i in range(0,n):
            if i == n-1:
                s = s + str(self.muestras[i]) + " ]"
            else:
                if j == 15:
                    s = s + str(self.muestras[i]) + ", \n  "
                    j = 0
                else:
                    s = s + str(self.muestras[i]) + ", "
                    j += 1
        print(s)

    """
    Method -- grafica()
    Método para graficar las muestras, haciendo uso del módulo matplotlib de python.
    """
    def grafica(self):
        plt.hist(self.muestras)
        plt.show()

