import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import random


def hiperGeometric(i,n,N,m):
    comb1 = (math.factorial(m))/((math.factorial(m-i))*math.factorial(i))
    comb2 = (math.factorial(N-m))/((math.factorial((N-m)-(n-1)))*math.factorial(n-1))
    comb3 = (math.factorial(N))/((math.factorial(N-n))*math.factorial(n))
    return comb1*comb2/comb3

class HyperGeometric:
    def __init__(self,size,N,m,noMuestras):
        self.size = size
        self.m = m
        self.N = N
        self.noMuestras = noMuestras
        self.muestras = self.simula()
    
    def simula(self):
        muestras = [0]*self.noMuestras
        for j in range(0,self.noMuestras):
            u = random.uniform(0,1)
            i = 0
            p = hiperGeometric(i,self.size,self.N,self.m)
            F = p
            while(i < min(self.size,self.m)):
                if u < F:
                    muestras[j] = i
                    break
                i += 1
                p = hiperGeometric(i,self.size,self.N,self.m)
                F = F + p
        return muestras
    
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
                  kde = True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
        ax.set(xlabel='BinNegative Distribution', ylabel='Frequency')
        plt.show()