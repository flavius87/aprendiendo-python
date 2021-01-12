import mysql.connector

# conexion
database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="master_python"
)

# print(database)

cursor = database.cursor(buffered=True)

# crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
) 
""")

# cursor.execute("INSERT INTO vehiculos values(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 20000),
    ('Mercedes', 'Clase C', 35000),
]
# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
result = cursor.fetchall()

print("-------Todos mis coches--------")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

# borrar

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
database.commit()

print(cursor.rowcount, "borrados")

# Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit()