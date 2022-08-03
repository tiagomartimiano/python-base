#!/usr/bin/python3

__version__ = "0.1.0"
__author__ = "Bruno"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros  = list(range(1, 11))

# Iterable (percorriveis)

# Para cada numero em numeros
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------")
    
