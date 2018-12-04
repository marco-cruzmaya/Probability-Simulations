import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from simulations.Poisson import Poisson
from simulations.Gamma import Gamma



class BinNegative:
    def __init__(self,r,p,noMuestras):
        self.r = r
        self.p = p
        self.noMuestras = noMuestras
        self.muestras = self.simula()
    
    def simula(self):
        muestra = [0]*self.noMuestras
        lmbda = (1-self.p)/self.p
        gamma = Gamma(self.r,lmbda,self.noMuestras)
        for k in range(0,self.noMuestras):
            y = gamma.gamma()
            poisson = Poisson(y,self.noMuestras)
            muestra[k] = poisson.poisson()
        return muestra
    
    def presentaMuestras(self):
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
    
    def grafica(self):
        ax = sns.distplot(self.muestras,
                  bins=100,
                  kde = False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='BinNegative Distribution', ylabel='Frequency')
        plt.show()