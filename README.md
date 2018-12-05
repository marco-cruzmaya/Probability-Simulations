# Probability-Simulations

Proyecto de simulaciones de alguanas funciones de distribución, como:

* **HyperGeometric**
* **Negative Binomial**
* **Poisson**
* **Gamma**

# Pre-Requisitos:

* Python 3

# Bibliotecas de Python: 
* matplotlib
* numpy
* seaborn

# Como se instalan:
```bash
$ python3 -m pip install numpy
$ python3 -m pip install matplotlib
$ python3 -m pip install seaborn
```

# Como se ejecuta cada programa:
```bash
$ sh Simulations.sh [Nombre de la distribución] [No. Muestras]
```
Después aparecera la parte de la inserción de los parámetros conrrespondientes a
la distribución.
* Para ejecutar poisson: [Nombre de la distribución] = Poisson o poisson, y sus parámetros a        insertar solo serían λ.
* Para ejecutar gamma: [Nombre de la distribución] = Gamma o gama, y sus parámetros a               insertar serían r y λ.
* Para ejecutar Hipergeometríca: [Nombre de la distribución] = HiperGeo o HiperGeometrica, y sus    parámetros a insertar serían n,N,m.
* Para ejecutar BinomialNegativa: [Nombre de la distribución] = BinNeg, BinNegative o binNegative,
  y sus párametros serían r y p.

