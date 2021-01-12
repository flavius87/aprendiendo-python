nombre = "Victor Robles"

# funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variables no es un número con decimales")

# Limpiar espacios
frase = " mi contenido "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2021
print(year)
del year
#print(year)

# comprobar la variable
texto = " ff "

if len(texto) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido", len(texto))

# encontrar caracteres
frase= "La vida es bella"
print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayúsculas y minúsculas
print(nombre)
print(nombre.lower())
print(nombre.upper())


