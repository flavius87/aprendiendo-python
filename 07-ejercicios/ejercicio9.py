"""
Ejercicio 9: hacer un programa que pida números al usuario indefinidamente
hasta meter el número 111.
"""
contador = 1
while contador < 100:
    numero =int(input("Elgie un número: "))
    if numero == 111:
        break
    else:
        print(f"Has introducido el {numero}")
        

