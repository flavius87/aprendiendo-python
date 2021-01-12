cantantes = ['Leon Gieco', 'Cerati', 'Miguel Bosse', 'Miguel Mateo']
numeros = [1, 2, 5, 8, 3, 4]

# ordenar
print(numeros)
numeros.sort()
print(numeros)

# añadir elementos
cantantes.append("Cosme Fulanito")
print(cantantes)
cantantes.insert(1, "David Bisbal")
print(cantantes)

"""
# Eliminar elementos de una lista
cantantes.pop(2)
cantantes.remove("Miguel Bosse")
print(cantantes)
"""

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Cerati' in cantantes)

# contar elementos
print(len(cantantes))
print(cantantes)

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Cosme Fulanito"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)