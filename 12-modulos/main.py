"""
Modulos: son funcionalidades ya hechas para reutilizar.
En python, por defecto, hay muchos modulos.
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, modulos en internet, 
y también podemos crear nuestros propios modulos.
"""
# import mimodulo
# importar funciones específicas de un módulo.
# from mimodulo import holaMundo
from mimodulo import * 
# print(mimodulo.holaMundo("Flavio Scheck WEB"))
# print(mimodulo.calculadora(3, 5, True))
print(holaMundo("Flavio Scheck WEB"))
print(calculadora(3, 5, True))

# modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada: ", fecha_personalizada)
print(datetime.datetime.now().timestamp())

# modulo matemáticas
import math

print("Raiz cuadrada de 10 es: ", math.sqrt(10))

print("Número pi: ", float(math.pi))

print("Redondear: ", math.ceil(6.325879))

# modulo random
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))