"""
Ejercicio 7: hacer un programa que muestre todos los números impares
entre dos números que elija el usuario.
"""

numero1 =int(input("Elige el primer número: "))
numero2 =int(input("Elige el segundo número: "))

if numero1 < numero2:
    for contador in range (numero1, (numero2 + 1)):
        if contador%2 != 0:
            print(contador)
else:
    print("El segundo número tiene que ser mayor al primero.")