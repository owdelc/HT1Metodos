import numpy as np
import matplotlib.pyplot as plt

def velocidad_iniciales(M, g, k, Ta, Tb, Puntos=100, Show=True, Tabla=False):
    t = np.linspace(Ta, Tb, Puntos)
    v = np.sqrt((M * g) / k) * np.tanh(t * np.sqrt((g * k) / M))
    
    if Tabla:
        print("Tabla de resultados:")
        print("Tiempo (segundos)\tVelocidad (metros/segundo)")
        for i in range(len(t)):
            print("\t{:.2f}\t\t\t{:.2f}".format(t[i], v[i]))
    
    if Show:
        plt.plot(t, v)
        plt.xlabel("Tiempo (segundos)")
        plt.ylabel("Velocidad (metros/segundo)")
        plt.title("Velocidad del objeto para M = {}, g = {}, y k = {}".format(M, g, k))
        plt.grid(True)
        plt.show()
    
    return t, v

def OndaTriangular(A, L):
    x = np.linspace(-2 * L, 4 * L, 1000)

    T = []

    for y in x:
        if -2*L <= y < -L:
            T.append((2*A) + ((A/L)*y))
        elif -L <= y < 0:
            T.append(-(A/L)*y)
        elif 0 <= y < L:
            T.append((A/L)*y)
        elif L <= y < 2*L:
            T.append((2*A) - ((A/L)*y))
        elif 2*L <= y < 3*L:
            T.append(((A/L)*y) - 2*A)
        elif 3*L <= y < 4*L:
            T.append(4*A - ((A/L)*y))
        else:
            T.append(0)

    return x,T


def graphOndaTriangular(X, T, A, L):
    plt.plot(X, T)
    plt.xlabel('x')
    plt.ylabel('T(x)')
    plt.title('Función Onda Triangular para A = {} y L = {}'.format(A, L))
    plt.grid(True)
    plt.show()

    return