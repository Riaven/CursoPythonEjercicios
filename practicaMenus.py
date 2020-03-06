from tkinter import *
from tkinter import messagebox #para poder hacer ventanas emergentes

root = Tk()

# PARA PONER CREAR UN MENSAJE EN VENTANA EMERGENTE #
def mostrarInfo():
    # showInfo() resibe dos parámetros, el titulo de la ventana  y el contenido de la misma#
    messagebox.showinfo("Acerca de ", "Procesador simple versión 1.0, 2020")
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
   
# Realiza pregunta al usuari si es que desea salir de la aplicación#
def salirAplicacion():
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?") 
    ## messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"), devuelve un booleano
    if respuesta == messagebox.YES:
        root.destroy()

def cerrarDocumento():
    messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento") #devuelve booleano

    #true = reintentar
    # false = cancelar#


# Para añadir un menú a la ventana#
barra = Menu(root)# Se ubica dentro de la raiz pero no se visualiza#
# Para visualizar#
root.config(menu=barra, width = 300, height = 300) # Se le dice que la barra anteriormente creada hace de menu en la ventana#
# Se especifican las diferentes opciones del menu#
archivoMenu = Menu(barra, tearoff = 0) # tearoff, es para que no salga una opcion por defecto que tiene el menu
archivoMenu.add_command(label ="Nuevo")
archivoMenu.add_command(label ="Guardar")
archivoMenu.add_command(label ="Guardar como...")
archivoMenu.add_separator() # se añade un separador entre las opciones del menu
archivoMenu.add_command(label ="Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label ="Salir", command = salirAplicacion)

archivoEdicion= Menu(barra, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas = Menu(barra, tearoff = 0)

archivoAyuda = Menu(barra, tearoff = 0)
archivoAyuda.add_command(label = "Licencia", command = avisoLicencia)
archivoAyuda.add_command(label = "Acerca de..." ,command = mostrarInfo)

# aqui es donde se agregan a la ventana
barra.add_cascade(label = "Archivo", menu = archivoMenu)
barra.add_cascade(label = "Edición", menu = archivoEdicion)
barra.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barra.add_cascade(label = "Ayuda", menu = archivoAyuda)
root.mainloop()