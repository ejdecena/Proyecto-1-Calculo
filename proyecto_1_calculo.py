#!/usr/bin/env python3
"""
Proyecto sobre Python y el workflow Pull-Request en GitHub.

Cada participante debe completar su función y luego solicitar el Pull-Request.
"""


def Ashly_Scarpati(a, b, c):
    """
    Recibe como parámetros los valores a, b, c y retorna el mínimo de a, b y c.
    """
    return


def Elder_Gomes(lista):
    """
    Recibe como parámetro una lista y retorna el mínimo valor de la lista.
    """
    return


def Hector_Salazar(tupla):
    """
    Recibe como parámetro una tupla y retorna el primer elemento de la tupla.
    """
    return tupla[0]


def Jose_Gomez(cadena):
    """
    Recibe como paŕametro una cadena y retorna el número de caracteres de la cadena.
    """
    cantidad = 0
    while cadena[cantidad:]:
            cantidad += 1
    return cantidad


def Lewis_Narvaez(tupla):
    """
    Recibe como parámetro una tupla y retorna el último elemento de la tupla.
    """
    return tupla[-1]


def Luisana_Hernandez(a, b, c):
    """
    Recibe como parámetros a, b, c y retorna el máximo de a, b, c.
    """
    return


def Lusandre_Marcano(conjunto):
    """
    Recibe como parámetros un conjunto y retorna el máximo del conjunto.
    """
    return max(conjunto)

if __name__ == "__main__":
    # Testing ...

    a = 1
    b = 5
    c = 7

    lista    = [a, b, c]
    tupla    = (a, b, c)
    conjunto = {a, b, c}
    cadena   = "Universidad de Oriente"

    if Ashly_Scarpati(a, b, c) == min(a, b, c):
        res = "10"
    else:
        res = "5"
    res = 0
    print("Ashly Scarpati:", res)

    if Elder_Gomes(lista) == min(lista):
        res = "10"
    else:
        res = "5"
    res = 0
    print("Elder Gomes:", res)

    if Hector_Salazar(tupla) == tupla[0]:
        res = "10"
    else:
        res = "5"
    print("Hector Salazar:", res)

    if Jose_Gomez(cadena) == len(cadena):
        res = "10"
    else:
        res = "5"
    print("Jose Gomez:", res)

    if Lewis_Narvaez(tupla) == tupla[-1]:
        res = "10"
    else:
        res = "5"
    print("Lewis Narvaez:", res)

    if Luisana_Hernandez(a, b, c) == max(a, b, c):
        res = "10"
    else:
        res = "5"
    print("Luisana Hernandez:", res)

    if Lusandre_Marcano(conjunto) == max(conjunto):
        res = "10"
    else:
        res = "5"
    print("Lusandre Marcano:", res)