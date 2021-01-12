"""
Ejercicio 1
Hacer un programa que tenga 8 números enteros:
-Recorrer la lista y mostrarla
-Hacer función que recorra lista de números y devuelva un string
-Ordenarla y mostrarla
-Mostrar longitud
-Buscar algún elemento (que el usuario pida por teclado)
"""

numeros = [8, 15, 2, 5, 1, 22, 0, 7]

# Recorrer lista y devolver string
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += ("\n")
    
    return resultado

# Recorrer y mostrar lista
"""
for numero in numeros:
    print(numero)

print("\n")
"""
print(mostrarLista(numeros))

print("\n")

# ordenar lista
numeros.sort()
print(mostrarLista(numeros))

# mostrar longitud
print(len(numeros))

# Buscar elemento pedido por el usuario

try:
    busqueda = int(input("Introduce el número: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")
    print(f"###### Buscar en la lista el número {busqueda} ###########")

    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el índice {search}")
except:
    print("El número no está en la lista. Lo siento.")