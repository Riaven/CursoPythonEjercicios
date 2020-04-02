# Para la base de datos #
import sqlite3
# Importar lo necesario para la ventana
from tkinter import *
# Importar ventanas emergentes
from tkinter import messagebox
################### CREACION DE CLASE USUARIO

class DatosUsuario():
    def __init__(self, iden, nombre, password, apellido, direccion, comentarios):
        self.__iden = iden
        self.__nombre = nombre
        self.__password = password
        self.__apellido = apellido
        self.__direccion = direccion
        self.__comentarios = comentarios 
    #get
    def getIden(self):
        return self.__iden
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
    CREATE TABLE DATOSPERSONA (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) ,
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
    try:
        cursor.execute(tabla_sql)
        messagebox.showinfo("Base de datos creada", "Base de datos creada correctamente")
    except:
        messagebox.showwarning("Base de datos ya existe", "Base de datos ya se encuentra creada y activa")
    return conex
    

# Operación busca usuario por su id dentro de la base de datos #
def buscarUsuario(id):
    '''
    Busca el usuario dentro de la base de datos, devuelve NONE si es que no existe
        Parámetros:
        id = int
    '''
    # Verifica que el tipo de dato entrante sea un int, ya que si fuera otro tipo de dato
    # la consulta genera un error, si es que no es un int, id se cambia por el valor -1#
    if type(id) != int:
        id = -1
    sql = "SELECT * FROM {} WHERE ID = {}".format(nombre_tabla,id)
    con = abreConexion()
    cursor = con.cursor()
    cursor.execute(sql)
    datos = cursor.fetchall()
    if len(datos) > 0:
        #extracción de datos individuales
        iden = datos[0][0]
        nombre = datos[0][1]
        password = datos[0][2]
        apellido = datos[0][3]
        direccion = datos[0][4]
        comentarios = datos[0][5]
        # Retorna el usuario completo para poder rellenar dato por dato
        return DatosUsuario(iden, nombre, password, apellido, direccion, comentarios)
    else:
        return None

    con.close()

#print(buscarUsuario(5)) #Prueba

################## Realizando el sistema crud con la base de datos 
def crea_usuario(nombre, password, apellido, direccion, comentarios):
    sql = "INSERT INTO " + nombre_tabla + " VALUES (NULL, ?,?,?,?,?)"
    datos = (nombre, password, apellido, direccion, comentarios) 
    con = abreConexion()
    cursor = con.cursor()
    cursor.execute(sql, datos)
    con.commit()
    con.close()

#crea_usuario('benito', "23", "Perez", "Calle falsa", "Buena persona eh") #Prueba

################ Operación que permite eliminar un usuario de la tabla en la base de datos
def eliminar_usuario(id):
    if buscarUsuario(id) != None:
        sql = '''
            DELETE FROM DATOSPERSONA
            WHERE ID = {}
        '''.format(id)
        con = abreConexion()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    else:
        print('Error. Usuario a eliminar no encontrado')

#eliminar_usuario(8) # Prueba
# Modifica los valores que contiene cierto usuario, dado su id #
def modificar_usuario(id, datos_nuevos):
    if buscarUsuario(id) != None :
        sql = '''UPDATE {tabla} SET NOMBRE = '{nombre}',
                                    PASSWORD = '{contrasena}',
                                    APELLIDO = '{apellido}',
                                    DIRECCION = '{direccion}',
                                    COMENTARIOS = '{comentarios}'  
                 WHERE ID={identi}'''.format(tabla = nombre_tabla, 
                                             nombre = datos_nuevos.getNombre(),
                                             contrasena = datos_nuevos.getPassword(), 
                                             apellido = datos_nuevos.getApellido(),
                                             direccion = datos_nuevos.getDireccion(),
                                             comentarios = datos_nuevos.getComentarios(), 
                                             identi = id)
        
        con = abreConexion()
        cursor = con.cursor()
        cursor.execute(sql) # Ejecuta la sentencia #
        con.commit() #Ejecuta los cambios dentro de la base de datos#
        con.close()
    else:
        print('Error. Usuario a modificar no encontrado')


###############
###############
#                VENTANA
###############
#Base de la ventana
root = Tk()
root.title("Práctica")
#Frame
frame = Frame(root)
frame.pack()

#Labels#
lbl_id = Label(frame, text= "ID")
lbl_id.grid(row = 0, column = 0, sticky = "e")

lbl_nombre = Label(frame, text= "NOMBRE")
lbl_nombre.grid(row = 1, column = 0, sticky = "e")

lbl_password = Label(frame, text= "PASSWORD")
lbl_password.grid(row = 2, column = 0, sticky = "e")

lbl_apellido = Label(frame, text= "APELLIDO")
lbl_apellido.grid(row = 3, column = 0, sticky = "e")

lbl_direccion = Label(frame, text= "DIRECCIÓN")
lbl_direccion.grid(row = 4, column = 0, sticky = "e")

lbl_comentarios = Label(frame, text= "COMENTARIOS")
lbl_comentarios.grid(row = 5, column = 0, sticky = "en")


#Entradas#
id_obtenido = StringVar()
id_obtenido.set("")
id_entry = Entry(frame, textvariable = id_obtenido)
id_entry.grid(row = 0, column = 1, pady = 10, padx = 10, columnspan = 4)

nombre_obtenido = StringVar()
nombre_obtenido.set("")
nombre_entry = Entry(frame, textvariable = nombre_obtenido)
nombre_entry.grid(row = 1, column = 1, pady = 10, padx = 10, columnspan = 4)

pass_obtenida = StringVar()
pass_obtenida.set("")
password_entry =  Entry(frame, textvariable = pass_obtenida)
password_entry.grid(row = 2, column = 1, pady = 10, padx = 10, columnspan = 4)
password_entry.config(show = "*") #Para que muestre otro  caracter, para proteger la contraseña


apellido_obtenido = StringVar()
apellido_obtenido.set("")
apellido_entry =  Entry(frame, textvariable = apellido_obtenido)
apellido_entry.grid(row = 3, column = 1, pady = 10, padx = 10, columnspan = 4)

direccion_obtenida = StringVar()
direccion_obtenida.set("")
direccion_entry =  Entry(frame, textvariable = direccion_obtenida)
direccion_entry.grid(row = 4, column = 1, pady = 10, padx = 10, columnspan = 4)

#comentarios_obtenidos = StringVar()
#comentarios_obtenidos.set("")
comentarios_text =  Text(frame, width = 16, height = 5)
comentarios_text.grid(row = 5, column = 1, pady = 10, padx = 10, columnspan = 4)


scroll = Scrollbar(frame, command = comentarios_text.yview)
scroll.grid(row = 5, column = 5, sticky = "nesw")
comentarios_text.config(yscrollcommand = scroll.set)

###########################
############################
#  FUNCIONES DE VENTANA##

def toma_datos():
    return DatosUsuario(id_obtenido.get(),
                        nombre_obtenido.get(),
                        pass_obtenida.get(),
                        apellido_obtenido.get(),
                        direccion_obtenida.get(),
                        comentarios_text.get(1.0, END))


def pintar_ventana():
    if len(id_obtenido.get())>0: # Corrobora que el parámetro id tenga contenido #
        datos = buscarUsuario(id_obtenido.get())
        if datos != None: # comprueba que el usuario se ha encontrado y rescatado los datos
            id_obtenido.set(datos.getIden())
            nombre_obtenido.set(datos.getNombre())
            pass_obtenida.set(datos.getPassword())
            apellido_obtenido.set(datos.getApellido())
            direccion_obtenida.set(datos.getDireccion())
            comentarios_text.insert(1.0, datos.getComentarios())
        else:
            messagebox.showerror("Usuario no encontrado", "Usuario con id {} no encontrado dentro de la base de datos".format(id_obtenido.get()))
    else:
        messagebox.showwarning(title = "Campo ID vacío", message = "Campo vacío, no es posible realizar la operación")
# limpia los campos #
def vaciar_ventana():
    id_obtenido.set("")
    nombre_obtenido.set("")
    pass_obtenida.set("")
    apellido_obtenido.set("")
    direccion_obtenida.set("")
    comentarios_text.delete(1.0, END)

# Modificar #
def llamar_modificar():
    if id_obtenido.get() != "" and nombre_obtenido.get()!="" and pass_obtenida.get()!="" and apellido_obtenido.get()!= "" and direccion_obtenida.get()!="" and comentarios_text.get(1.0, END)!="":
        if buscarUsuario(id_obtenido.get()):
            pregunta = messagebox.askyesno("Modificar", "¿Desea modificar al usuario {}?".format(id_obtenido.get()))
            if pregunta == True:

                modificar_usuario(id_obtenido.get(), DatosUsuario(id_obtenido.get(),
                                                                nombre_obtenido.get(),
                                                                pass_obtenida.get(),
                                                                apellido_obtenido.get(),
                                                                direccion_obtenida.get(),
                                                                comentarios_text.get(1.0, END)))
                messagebox.showinfo(title = "Usuario modificado", message= "Usuario se ha modificado correctamente")
        else:
            messagebox.showerror(title= "Usuario no encontrado", message="Error al modificar, usuario no se ha encontrado en la base de datos")
    else:
        messagebox.showwarning(title="Campos vacíos", message= "No es posible realizar la operación")
# comprueba que las entradas no esten vacias y llama al método para crear nuevos usuarios #
def llamar_crear():
    if nombre_obtenido.get()!="" and pass_obtenida.get()!="" and apellido_obtenido.get()!= "" and direccion_obtenida.get()!="" and comentarios_text.get(1.0, END)!="":
        crea_usuario(nombre_obtenido.get(),
                     pass_obtenida.get(),
                     apellido_obtenido.get(),
                     direccion_obtenida.get(),
                     comentarios_text.get(1.0, END))
        messagebox.showinfo(title = "Usuario creado", message= "Usuario se ha guardado dentro de la base de datos correctamente")
        
    else:
        messagebox.showwarning(title="Campos vacíos", message="No se permiten campos vacíos")


#llama a función eliminar usuario, preguntando si es este existe primero#
def llama_eliminar():
    if id_obtenido.get() != "":
        if buscarUsuario(id_obtenido.get()):
            pregunta = messagebox.askyesno("Eliminar", "¿Desea eliminar al usuario {}?".format(id_obtenido.get()))
            if pregunta == True:
                eliminar_usuario(id_obtenido.get())
                messagebox.showinfo(title = "Éxito",message= "Usuario {} eliminado con éxito dentro de la base de datos".format(id_obtenido.get()))
        else:
            messagebox.showerror(title="Usuario no encontrado", message="Error al eliminar usuario con id {}, no se encuentra en la base de datos".format(id_obtenido.get()))
    else:
        messagebox.showwarning(title = "Campo vacío ", message = "Error al realizar operación")

def salir():
    pregunta = messagebox.askyesno("Salir", "¿Desea salir de la aplicación?")
    if pregunta == True:
        root.destroy()
########################
########################
#    MENUS################
barra = Menu(root)
root.config(menu = barra, width =300, height = 300)
bbdd_menu = Menu(barra, tearoff = 0)
bbdd_menu.add_command(label = "Abrir base de datos", command = abreConexion)
bbdd_menu.add_command(label = "Salir", command = salir)

borrar_menu = Menu(barra, tearoff = 0)
borrar_menu.add_command(label = "Limpiar pantalla", command = vaciar_ventana)

crud_menu = Menu(barra, tearoff = 0)
crud_menu.add_command(label = "Buscar", command = pintar_ventana)
crud_menu.add_command(label = "Modificar", command = llamar_modificar)
crud_menu.add_command(label = "Eliminar", command = llama_eliminar)
crud_menu.add_command(label = "Crear", command = llamar_crear)

barra.add_cascade(label = "BBDD",  menu = bbdd_menu)
barra.add_cascade(label = "Borrar", menu = borrar_menu)
barra.add_cascade(label = "CRUD", menu = crud_menu)
################

# BOTONES #
boton_buscar = Button(frame, text = "Buscar", command = pintar_ventana)
boton_buscar.grid(row = 6, column = 0,pady = 5, padx = 5, sticky = "e" )

boton_modificar = Button(frame, text = "Modificar", command = llamar_modificar)
boton_modificar.grid(row = 6, column = 1 ,  pady = 5, padx = 5)

boton_eliminar = Button(frame, text = "Eliminar", command = llama_eliminar)
boton_eliminar.grid(row = 6, column = 2 ,  pady = 5, padx = 5)

boton_crear = Button(frame, text = "Crear", command = llamar_crear )
boton_crear.grid(row = 6, column = 3 ,  pady = 5, padx = 5)

#Mantener la ventana abierta
root.mainloop()
