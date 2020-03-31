import sqlite3
conexion = sqlite3.connect("GestionProductos")# crea e inicia la conexión
cursor = conexion.cursor()# Para poder ejecutar acciones dentro de la base de datos
# Se crea una nueva tabla en la base de datos
# 
# Para que la clave primaria se vaya autoincrementando sola, 
# es conveniente denominarla id mas el AUTOINCREMENT #

cursor.execute('''
    CREATE TABLE PRODUCTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')
# productos es una lista de tuplas #
productos=[
    ("pelota", 20, "jugeteria"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
conexion.commit()# produce los cambios dentro de la base de datos
conexion.close() # Cierra la base de datos#