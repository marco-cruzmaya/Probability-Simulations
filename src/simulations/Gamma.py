import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math

class Gamma:
    def __init__(self,r,lmbda,noMuestras):
        self.r = r
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
            muestras[j] = self.gamma()
        return muestras
    
    """
    Method(auxiliar) -- gamma()
    @return X: Dondé X es una variable aleatoria que se distribuye Gamma.
    Método auxliar para crear una variable aleatoria que se destribuye Gamma con
    párametros n, lamda.
    """

    def gamma(self):
        x = 0
        for i in range(0,self.r):
            u = random.uniform(0,1)
            exp = math.pow(-1*self.lmbda,-1)*(math.log(1-u))
            x = x + exp
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
    Método para graficar las muestras, haciendo uso del módulo seaborn de python.
    """

    def grafica(self):
        ax = sns.distplot(self.muestras,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='Gamma Distribution', ylabel='Frequency')
        plt.show()