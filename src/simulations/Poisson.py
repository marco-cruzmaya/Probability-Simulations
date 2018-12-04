import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math


class Poisson:
    def __init__(self, lmbda, noMuestras):
        self.lmbda = lmbda
        self.noMuestras = noMuestras
        self.muestras = [0]*noMuestras
    
    """
    Method --simula()
    Método para crear las muestras a simular.
    """
    def simula(self):
        muestras = [0]*self.noMuestras
        for j in range(0,self.noMuestras):
            muestras[j] = self.poisson()
        return muestras
    
    def poisson(self):
        x = 0
        u = random.uniform(0,1)
        p = math.exp(-1*self.lmbda)
        F = p
        i = 0
        while(True):
            if u < F:
                x = i
                break
            i += 1
            p = (self.lmbda*p)/(i)
            F = F + p
        return x
    """
    Method -- presentaMuestras()
    Método para mejorar la representación de cadena del arreglo de muestras.
    """
    def presentaMuestras(self):
        self.muestras = self.simula()
        n = len(self.muestras) #longitud del arreglo
        s = "[ "
        j = 0
        if n == 0:
            return s + "]"
        for i in range(0,n):
            if i == n-1:
                s = s + str.format("%.2f" % self.muestras[i]) + " ]"
            else:
                if j == 15:
                    s = s + str.format("%.2f" % self.muestras[i]) + ", \n  "
                    j = 0
                else:
                    s = s + str.format("%.2f" % self.muestras[i]) + ", "
                    j += 1
        print(s)

    """
    Method -- grafica()
    Método para graficar las muestras, haciendo uso del módulo matplotlib de python.
    """
    def grafica(self):
        if len(self.muestras) > 1:
            ax = sns.distplot(self.muestras,
                    kde=True,
                    bins=100,
                    color='skyblue',
                    hist_kws={"linewidth": 15,'alpha':1})
            ax.set(xlabel='Poisson Distribution', ylabel='Frequency')
            plt.show()

