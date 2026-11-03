
import pytest

from calculadora import sumar, multiplicar

def test_suma():
    assert sumar(5, 3) == 8

def test_multiplicacion():
    assert multiplicar(4, 5) == 20

from calculadora import (
    sumar, restar, multiplicar, dividir,
    potencia, raiz_cuadrada, porcentaje, modulo
)


@pytest.mark.parametrize("a,b,esperado", [
    (5, 3, 8),
    (-5, 2, -3),
    (0, 7, 7)
])
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.parametrize("a,b,esperado", [
    (10, 4, 6),
    (3, 8, -5),
    (5, 5, 0)
])
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado


@pytest.mark.parametrize("a,b,esperado", [
    (4, 5, 20),
    (-3, 2, -6),
    (0, 9, 0)
])
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado


@pytest.mark.parametrize("a,b,esperado", [
    (20, 4, 5),
    (7, 2, 3.5)
])
def test_dividir(a, b, esperado):
    assert dividir(a, b) == esperado


def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


@pytest.mark.parametrize("a,b,esperado", [
    (2, 3, 8),
    (5, 0, 1)
])
def test_potencia(a, b, esperado):
    assert potencia(a, b) == esperado


@pytest.mark.parametrize("numero,esperado", [
    (25, 5),
    (0, 0)
])
def test_raiz(numero, esperado):
    assert raiz_cuadrada(numero) == esperado


def test_raiz_negativa():
    with pytest.raises(ValueError):
        raiz_cuadrada(-9)


def test_porcentaje():
    assert porcentaje(200, 15) == 30


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_entre_cero():
    with pytest.raises(ValueError):
        modulo(10, 0)
