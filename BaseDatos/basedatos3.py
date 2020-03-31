# Leer datos desde la base de datos #
import sqlite3
conexion = sqlite3.connect("GestionProductos")# Como parámetro se envía el nombre de la base de datos #
# Se crea un cursor para poder realizar acciones dentro de la base de datos#
cursor = conexion.cursor()

cursor.execute("SELECT *  FROM PRODUCTOS WHERE SECCION = 'jugeteria'")

recibe_productos = cursor.fetchall()

print(recibe_productos)

# Para que los cambios se realicen correctamente dentro de la base de datos #
conexion.commit()
# Siempre se debe de cerrar la base de datos al final del archivo o de la acción #
conexion.close()


