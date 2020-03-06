from tkinter import *
from tkinter import filedialog # Para poder añadir la ventana de abrir archivo#
root = Tk()

# Función para abrir una carpeta #
def abrirCarpeta():
    # title = corresponde al título que tendra la ventana emergente
    # initialdir =  corresponde al directorio que por defecto abre primero la ventana emergente#
    carpeta = filedialog.askopenfilename(title = "Abrir", initialdir = "C:", filetypes = (("Ficheros Excel", "*.xlsx"),
                                                                                          ("Ficheros de texto", "*.txt")))
    

Button(root, text = "Abrir", command = abrirCarpeta).pack()
root.mainloop()