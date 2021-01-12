"""
Ejercicio 5. Hacer un programa que muestre todos los números
entre dos números que diga el usuario.
"""
numero1 =int(input("Elige el primer número: "))
numero2 =int(input("Elige el segundo número: "))

if numero2 > numero1:
    for contador in range(numero1, numero2 +1):
        print(contador)
else:
    print("El segundo número tiene que ser mayor al primero.")
