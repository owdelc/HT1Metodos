import funciones as fun


# Ejercicio 1

# Parte (b)
M = 50
g = 9.8
k = 0.5
Ta = 0
Tb = 20
Puntos = 21
Show = False
Tabla = True

t, v = fun.velocidad_iniciales(M, g, k, Ta, Tb, Puntos, Show, Tabla)

# Parte (c)
M = 50
g = 9.8
k = 0.5
Ta = -10
Tb = 10

t, v = fun.velocidad_iniciales(M, g, k, Ta, Tb)

###################################################

# Ejercicio 2

import numpy as np
import matplotlib.pyplot as plt

# b)
A = 6
L = 2
X,T = fun.OndaTriangular(A, L)
fun.graphOndaTriangular(X, T, A, L)

# c)

A = -2
L = 4
X,T = fun.OndaTriangular(A, L)
fun.graphOndaTriangular(X, T, A, L)
