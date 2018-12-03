import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Gamma:
    def __init__(self,n,lmbda,noMuestras):
        self.n = n
        self.lmbda = lmbda
        self.noMuestras = noMuestras
        self.muestras = self.simula()
    
    def simula(self):
        return np.random.gamma(self.n,self.lmbda,self.noMuestras)
    
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
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='Gamma Distribution', ylabel='Frequency')
        plt.show()