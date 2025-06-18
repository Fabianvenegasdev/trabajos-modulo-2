import math

# Calcula el área de un círculo dado su radio
def area_circulo(radio):
    return math.pi * radio ** 2

# Devuelve el área de un rectángulo usando ancho y alto
def area_rectangulo(ancho, alto):
    return ancho * alto

# Encuentra el área de un triángulo con base y altura
def area_triangulo(base, altura):
    return (base * altura) / 2

# Calcula el factorial de un número
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Verifica si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True