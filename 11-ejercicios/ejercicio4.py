"""
Ejercicio 4: crear un script que tenga 4 variables: lista, string, entero y
booleano. Que imprima un mensaje según el tipo de dato de cada variable.
Usar funciones.
"""
# variable lista
lista = [12, 15, 19, 8]

# variable string
string = "Hola, me llamo Flavio"

# variable entero
entero = 80

# booleano
booleano = False
"""
print(lista)
print(string)
print(entero)
print(booleano)

print("\n")

print(type(lista))
print(type(string))
print(type(entero))
print(type(booleano))

"""
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"

    return result

def comprobarTipado (dato,tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    
    return result

print(comprobarTipado(lista, list))
print(comprobarTipado (string, str))
print(comprobarTipado(entero, int))
print(comprobarTipado(booleano, bool))