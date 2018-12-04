import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math

class Gamma:
    def __init__(self,n,lmbda,noMuestras):
        self.n = n
        self.lmbda = lmbda
        self.noMuestras = noMuestras
        self.muestras = [0]*noMuestras
    
    def simula(self):
        muestras = [0]*self.noMuestras
        for j in range(0,self.noMuestras):
            muestras[j] = self.gamma()
        return muestras
    
    def gamma(self):
        x = 0
        for i in range(0,self.n):
            u = random.uniform(0,1)
            exp = math.pow(-1*self.lmbda,-1)*(math.log(1-u))
            x = x + exp
        return x
    
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
    
    def grafica(self):
        ax = sns.distplot(self.muestras,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='Gamma Distribution', ylabel='Frequency')
        plt.show()