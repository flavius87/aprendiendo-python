"""
Ejercicio 10. Programa tiene que pedir nota de 15 alumnos y sacar por 
pantalla quiénes han aprobado y cuántos han desaprobado.
"""

contador = 1
aprobados = 0
desaprobados = 0

numero_alumnos = int(input("Cuántos alumnos tienes? "))

while contador <= numero_alumnos:
    nota = int(input(f"Qué nota quieres ponerle al \"alumno{contador}\"?: "))
    if nota >= 5:
        aprobados += 1
    else:
        desaprobados += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos desaprobados: {desaprobados}")