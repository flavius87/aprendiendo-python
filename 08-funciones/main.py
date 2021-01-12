"""
Una función es un conjunto de instrucciones agrupadas bajo un mismo
nombre (o nombre concreto) que pueden reutilizarse invocando a la función 
tantas veces como sea necesario.

def nombreDeMiFunción(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFunción(mi_parametro)
"""
# Ejemplo 1
print("##### EJEMPLO 1 #####")

def muestraNombre():
    print("Flavio")
    print("Nestor")
    print("Fran")
    print("Cristian")
    print("Natalia")
    print("\n")

# invocar funciones
muestraNombre()
"""
# Ejemplo 2
print("##### EJEMPLO 2 #####")

def mostrartunombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
mostrartunombre(nombre, edad)
"""
# Ejemplo 3
print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del {numero}")

    for contador in range (11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")

tabla(3)
tabla(12)
tabla(7)

# Ejemplo 3.1
print("##### EJEMPLO 3.1 #####")

for numero_tabla in range (1,11):
    tabla(numero_tabla)


# Ejemplo 4
print("##### EJEMPLO 4 #####")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
   # print(f"DNI: {dni}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Victor Robles", "43562897")

print("\n")

# Ejemplo 5
print("##### EJEMPLO 5 #####")

# Return o devolver datos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Victor Robles"))

# Ejemplo 6
print("\n##### EJEMPLO 6 #####")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1+numero2
    resta = numero1-numero2
    multi = numero1*numero2
    division = numero1/numero2

    cadena = ""
    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "división: " + str(division)

    return cadena

print(calculadora(5, 5, True))

# Ejemplo 7
print("\n##### EJEMPLO 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre,apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Victor", "Robles"))

# Ejemplo 8
print("\n##### EJEMPLO 8 #####")

# Funciones Lamda. Son funciones anónimas. Sirven para tareas simples. 

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2025))
