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


def zodiacal():
    month = int(input("Ingresa el mes de nacimiento (Numero entre 1 y 12): "))
    day = int(input("Ingresa el dia de nacimiento: "))
    if month == 1 and day >= 20 or month == 2 and day <= 18:
        print("Actuario")
    elif month == 2 and day >= 19 or month == 3 and day <= 21:
        print("Piscis")
    elif month == 3 and day >= 21 or month == 4 and day <= 19:
        print("Aries")
    elif month == 4 and day >= 20 or month == 5 and day <= 20:
        print("Tauro")
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        print("Géminis")
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        print("Cáncer")
    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        print("Leo")
    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        print("Virgo")
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        print("Libra")
    elif month == 10 and day >= 23 or month == 11 and day <= 21:
        print("Escorpio")
    elif month == 11 and day >= 22 or month == 12 and day <= 21:
        print("Sagitario")
    else:
        print("Capricornio")


square()
triangle()
circle()

zodiacal()
