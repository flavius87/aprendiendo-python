"""
Ejercicio 6: mostrar todas las tablas de multiplicar del 1 al 10
Mostrando título de la tabla y las multiplicaciones.
"""

tabla1 = 1
tabla2 = 2
tabla3 = 3
tabla4 = 4
tabla5 = 5
tabla6 = 6
tabla7 = 7
tabla8 = 8
tabla9 = 9
tabla10 = 10

print("###### Tabla del 1 ###### ")

for tabla1 in range (1,11):
    print(tabla1*1)


print("------------------------------------")

for cabecera in range(1,11):
    print("################################")
    print(f"##### Tabla del {cabecera} #######")
    print("################################")

    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")
    
