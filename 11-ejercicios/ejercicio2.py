"""
Escribir un programa que agregue valores a una lista mientras que su longitud
sea menor a 120 y luego mostrar la lista.
Usar while y for.
"""
coleccion = []
"""
for contador in range (0,120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])
print(coleccion)
"""
contador = 0
coleccion = []

while contador < 120:
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])
    contador += 1

