
import math


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def potencia(a, b):
    return a ** b


def raiz_cuadrada(a):
    if a < 0:
        raise ValueError(
            "No se puede calcular la raiz de un negativo"
        )
    return math.sqrt(a)


def porcentaje(a, b):
    return (a * b) / 100


def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular modulo cero")
    return a % b


