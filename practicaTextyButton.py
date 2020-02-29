from tkinter import *

frame = Tk()
frame.title("Probando botón y text")
# Probando text, este es una caja para escribir con alta capacidad, si es 
# que se quiere agregar un scroll, debe de hacerse manualmente, ya que por
# defecto no esta agregado, además se debe de cambiar manualmente el tamaño
# ya que por defecto ya viene con un tamaño que puede modificar el frame#

lblBiografia = Label(text = "Biografía")
lblBiografia.grid(row = 0, column = 0)

#text
txtBiografia = Text(width = 16, height = 5) #por defecto sin scroll
txtBiografia.grid(row = 0, column = 1, pady = 15, padx = 15)
#Se debe de construir un scroll
scrollBio = Scrollbar(frame, command = txtBiografia.yview)
scrollBio.grid(row = 0, column = 2, sticky = "nesw")
#para que el Scroll baje cuando se escribe 
txtBiografia.config(yscrollcommand = scrollBio.set)
#código debe de ir antes de ser llamado, al ser un lenguaje interpretado
def codigoBoton():
    print("Botón me dice que tu nombre es: ", miNombre.get())
##boton
boton = Button(frame, text = "Aceptar", command=codigoBoton)
boton.grid(row = 3, column = 1)
miNombre = StringVar() #variable que tomara el valor que le de entry
entradaNombre = Entry(frame, textvariable = miNombre) #con textvariable, se puede ver o modificar el contenido que tiene la Entry
entradaNombre.grid(row = 2, column = 1)# se posiciona la entry dentro del frame con grid

frame.mainloop()