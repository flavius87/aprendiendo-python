from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir
archivo.write("######## soy un texto metido desde python #########\n")

# cerrar archivo
archivo.close()

# Abrir archivo para lectura
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# for elemento in contenido:
#    print(elemento)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# print(lista)
for frase in lista:
    if not frase.isnumeric():
        print("- "+frase.upper())

# Copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = "./07-ejercicios/fichero_copiado77.txt"
shutil.copyfile(ruta_original, ruta_nueva)
# shutil.copyfile(ruta_original, ruta_alternativa)
"""

"""
# Mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)
"""
"""
# Eliminar
import os
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""
# Comprobar si un archivo existe o no
import os.path
# print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
