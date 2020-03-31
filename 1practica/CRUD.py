# Para la base de datos #
import sqlite3
################### CREACION DE CLASE USUARIO

class DatosUsuario():
    def __init__(self, nombre, password, apellido, direccion, comentarios):
        self.__nombre = nombre
        self.__password = password
        self.__apellido = apellido
        self.__direccion = direccion
        self.__comentarios = comentarios 
    #get
    def getNombre(self):
        return self.__nombre
    
    def getPassword(self):
        return self.__password
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion

    def getComentarios(self):
        return self.__comentarios

########################
#      Conexion con base de datos
#################
nombre_bd = "GESTION"
nombre_tabla = "DATOSPERSONA"
tabla_sql = '''
    CREATE TABLE IF NOT EXISTS DATOSPERSONA (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) UNIQUE,
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(100),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(150)
    )
'''
# Abre la base de datos y crea la tabla si es que esta no existe #
def abreConexion():
    conex = sqlite3.connect("GESTION")
    cursor = conex.cursor()
    cursor.execute(tabla_sql)
    return conex

################## Realizando el sistema crud con la base de datos 
def crea_usuario(nombre, password, apellido, direccion, comentarios):
    sql = "INSERT INTO " + nombre_tabla + " VALUES (NULL, ?,?,?,?,?)"
    print(sql)
    datos = (nombre, password, apellido, direccion, comentarios) 
    con = sqlite3.connect(nombre_bd)
    cursor = con.cursor()
    cursor.execute(sql, datos)

crea_usuario('benito', "23", "Perez", "Calle falsa", "Buena persona eh")