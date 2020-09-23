import math


def square():
    side = input("Ingresa el lado del cuadrado: ")
    print("El area es: ", side)


def triangle():
    base = int(input("Ingresa la base del triangulo: "))
    height = int(input("Ingresa la altura del triangulo: "))
    print("El area es: ", base * height / 2)


def circle():
    radius = int(input("Ingresa el radio del circulo: "))
    print("El area es: ", math.pi * radius ** 2)


square()
triangle()
circle()
