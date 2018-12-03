import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class HyperGeometric:
    def __init__(self,Ngood,m,n,noMuestras):
        self.Ngood = n
        self.m = m
        self.n = n
        self.noMuestras = noMuestras
        self.muestras = self.simula()
    
    def simula(self):
        return np.random.hypergeometric(self.Ngood,self.m,self.n,self.noMuestras)
    
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
    
    def grafica(self):
        ax = sns.distplot(self.muestras,
                  bins=100,
                  kde = False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='BinNegative Distribution', ylabel='Frequency')
        plt.show()