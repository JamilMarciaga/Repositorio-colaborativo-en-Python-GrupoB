"""
PRUEBAS UNITARIAS - OPERACIONES MATEMATICAS
Responsable: Jamil Marciaga
Grupo B
"""

import pytest
from src.operaciones_matematicas import *

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-1, -1) == 0
    assert resta(0, 5) == -5

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-2, 3) == -6
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(5, 2) == 2.5
    with pytest.raises(ValueError):
        division(5, 0)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1

def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(16) == 4
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_promedio():
    assert promedio([1, 2, 3, 4, 5]) == 3
    with pytest.raises(ValueError):
        promedio([])

def test_es_primo():
    assert es_primo(7) == True
    assert es_primo(4) == False

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(0) == []

def test_maximo():
    assert maximo([1, 5, 3, 9, 2]) == 9
    with pytest.raises(ValueError):
        maximo([])

def test_minimo():
    assert minimo([1, 5, 3, 9, 2]) == 1
    with pytest.raises(ValueError):
        minimo([])