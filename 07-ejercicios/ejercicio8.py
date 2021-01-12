"""
Ejercicio 8: tenemos que hacer un programa que haga cuánto es el x %
de x número.
"""

numero =int(input("Introduce el número: "))
porcentaje =int(input("Introduce qué porcentaje quieres sacar del {numero}: "))

operacion = (numero * (porcentaje/100))

print(f"El %{porcentaje} de {numero} es: {operacion}")
