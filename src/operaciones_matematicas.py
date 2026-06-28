"""
MODULO DE OPERACIONES MATEMATICAS
Responsable: Jamil Marciaga
Grupo B
"""

import math

# ============================================
# OPERACIONES BASICAS
# ============================================

def suma(a, b):
    """Suma dos numeros"""
    return a + b

def resta(a, b):
    """Resta dos numeros"""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos numeros"""
    return a * b

def division(a, b):
    """Divide dos numeros"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# ============================================
# OPERACIONES AVANZADAS
# ============================================

def potencia(base, exponente):
    """Calcula la potencia de un numero"""
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raiz cuadrada de un numero"""
    if numero < 0:
        raise ValueError("No se puede calcular raiz de numero negativo")
    return math.sqrt(numero)

def factorial(n):
    """Calcula el factorial de un numero"""
    if n < 0:
        raise ValueError("No se puede calcular factorial de numero negativo")
    return math.factorial(n)

# ============================================
# ESTADISTICAS
# ============================================

def promedio(lista):
    """Calcula el promedio de una lista de numeros"""
    if not lista:
        raise ValueError("La lista no puede estar vacia")
    return sum(lista) / len(lista)

def mediana(lista):
    """Calcula la mediana de una lista de numeros"""
    if not lista:
        raise ValueError("La lista no puede estar vacia")
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

# ============================================
# FUNCIONES ESPECIALES
# ============================================

def es_primo(n):
    """Verifica si un numero es primo"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Genera los primeros n numeros de la serie Fibonacci"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# ============================================
# FUNCIONES ADICIONALES
# ============================================

def maximo(lista):
    """Encuentra el valor maximo en una lista"""
    if not lista:
        raise ValueError("La lista no puede estar vacia")
    return max(lista)

def minimo(lista):
    """Encuentra el valor minimo en una lista"""
    if not lista:
        raise ValueError("La lista no puede estar vacia")
    return min(lista)

# ============================================
# FUNCIONES ADICIONALES Gilberto Cano
# ============================================

def modulo(a, b):
    """Calcula el residuo de la división entre dos números"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a % b



# ============================================
# PRUEBA DEL MODULO
# ============================================

if __name__ == "__main__":
    print("Probando modulo de matematicas...")
    print("5 + 3 =", suma(5, 3))
    print("10 / 2 =", division(10, 2))
    print("2^3 =", potencia(2, 3))
    print("Raiz cuadrada de 16 =", raiz_cuadrada(16))
    print("5! =", factorial(5))
    print("Promedio [1,2,3,4,5] =", promedio([1, 2, 3, 4, 5]))
    print("Mediana [1,3,5,7,9] =", mediana([1, 3, 5, 7, 9]))
    print("7 es primo?", es_primo(7))
    print("Fibonacci(7) =", fibonacci(7))
    print("Maximo [1,5,3,9,2] =", maximo([1, 5, 3, 9, 2]))
    print("Minimo [1,5,3,9,2] =", minimo([1, 5, 3, 9, 2]))
    print("10 % 3 =", modulo(10, 3))

    print("Todo funciona correctamente")