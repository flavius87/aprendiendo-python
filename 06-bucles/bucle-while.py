"""
# Bucle while
Estructura de control que itera o repite la ejecución de una serie 
de instrucciones tantas veces como sea necesario, 
hasta que deje de cumplirse la condición.

while condición:
    bloque de instrucciones
    actualización de contador
"""

contador = 1
while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador = contador + 1

print("---------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + "," + str(contador) 
    contador += 1
print(muestrame)

print("#### EJEMPLO #########")
numero_usuario =int(input("De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
print(f"###### tabla del {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("Tabla terminada.")
    
