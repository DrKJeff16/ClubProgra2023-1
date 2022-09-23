#!/usr/bin/env python3
"""Ejemplos del uso de paréntesis y flujos de ejecución."""
import sys


# Encapsula la ejecución del código en un 'método main'.
if __name__ == '__main__':
    a = 9
    b = -10
    print((a + b))
    print(a + b)

    c = a + b / a
    d = (a + b) / a
    print(c == d)  # ¿Será 'c' igual a 'd'?

    print(a + b * 15 - 12 + c / d)

    # Primero se ejecuta 'input', y lo que retorne la función se pasa a 'int()'
    num_1 = int(input("Ingrese un número: "))

    # Primero se ejecuta 'input', y lo que retorne se le aplica el
    # Método 'split()' de la clase 'str', que retorna una lista.
    nums_1 = input("Ingrese números separados por un espacio: ").split(' ')

    # Primero se ejecuta 'input', y lo que retorne se le aplica el
    # Método 'split()' de la clase 'str', que retorna una lista.
    # Luego itera por cada elemento de esa lista, llamándolo 'a',
    # Y le aplica 'int()' para convertirlo a int.
    nums_2 = [int(a) for a in input("Ingrese más números separados: ").split(' ')]

    print(num_1)
    print(nums_1)
    print(nums_2)

    sys.exit(0)  # Sal del script con éxito
