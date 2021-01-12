"""
Ejercicio 3: programa que compruebe si una variable está vacía.
Y si está vacía rellenarla con texto en minúscula y mostrarlo en mayúsculas.
"""

# comprobar variable
texto = ""
if len(texto.strip()) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido", len(texto))

variable_vacia = "piletazo"

if len(texto) <= 0:
    print(variable_vacia)
    print(variable_vacia.upper())

