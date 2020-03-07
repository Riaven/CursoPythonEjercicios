import sqlite3 # se importa el paquete para poder acceder a la maniputación de una base de datos sqlite#

# Se abre la conexión con el método connect(), indicando el nombre de la base de datos,
# Si es que esta no está creada, la crea en el instante, de ser llamada#
conexion = sqlite3.connect("Tienda")
# Se crea un puntero o cursor, que se encarga de manipular la base de datos #
cursor = conexion.cursor()
# Con el cursor se crea una nueva tabla#
#cursor.execute("CREATE TABLE Productos (nombre_articulo VARCHAR(50), precio INTEGER , tipo VARCHAR(20))")


# en el caso de querer insertar más de un producto a la vez, se puede de insertar con
# una tupla#
'''
productos = [
    ("Camiseta", 5000, "Torso"),
    ("Polera", 3000,  "Torso"),
    ("Pantalón", 5000,  "Pierna"),
    ("Calcetines", 2000,  "Pierna"),
    ("Pantaleta", 4000,  "Pierna"),
    ("Blusa", 7000,  "Torso"),
    ("Camisa", 2500,  "Tors")
]

# Para ejecutar muchos a la misma vez#
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)
'''
# Para hacer un select y poder tomar los datos que devuelve la consulta#
cursor.execute("SELECT * FROM Productos")
todos = cursor.fetchall() # todos los productos que devuelve la sentencia select /// devuelve una lista con los datos#
for producto in todos:
    print(producto)
# Para que se ejecute todo lo anterior se debe de autorizar a la base de datos#
conexion.commit()

#datos = cursor.execute("SELECT * FROM Productos")

conexion.close() #Se cierra la conexión

