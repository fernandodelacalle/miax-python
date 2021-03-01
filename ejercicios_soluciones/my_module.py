import math
import random


def area_circulo(r=1):
    return math.pi*(r**2)


def lista_uniforme(n):
    lista_al = []
    for _ in range(n):
        n_al = random.uniform(0, 10)
        lista_al.append(n_al)
    return lista_al


def suma_elementos(x, y):
    return x+y