"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/ valores, bajo un único nombre.
Para acceder a esos valores tenemos que acceder a un índice numérico.
"""

# Definir Listas
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('Roxette', 'Soda Stereo', 'Radiohead'))
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4, True, "Texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
# indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# añadir elementos a lista
cantantes.append("Leon Gieco")
print(cantantes)


# Recorrer lista
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una nueva película: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
"""
print("\n##### LISTADO DE PELICULAS ######")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Listas multidimensionales
print("\n###### LISTADO DE CONTACTOS ######")
contactos = [
    [
        'Antonio',
        'antonio@puntocom.com',
    ],
    [
        'Luis',
        'luis@hotmail.com',
    ],
    [
        'Gerónimo',
        'gero_45@gmail.com',
    ],
    [
        'Patricia',
        'pato81@yahoo.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")


# print(contactos)