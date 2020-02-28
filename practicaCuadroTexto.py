#se importa la libreria a usar
from tkinter import *
#se crea la raiz
root = Tk()
#frame
frame = Frame(root, width = 400, height = 500)
frame.pack()
#crear el cuadro de texto dentro de la raiz
entrada = Entry(frame)
#empaquetar
entrada.grid(row = 0, column = 1, pady=10)
label =  Label(frame, text = "Nombre") #nombre para el cuadro de texto
# Por defecto los label dentro de la grid, se posicionan al centro
# Si es que se quisiera posicionar al gusto debe de usarse 
# el método sticky()#
# La posición se dará  usando los puntos cardinales N, S, E, O, 
# tambien hay puntos intermedios NE = noreste#
label.grid(row = 0, column = 0, sticky="W", pady=10) #se posiciona a la izquierda
# pady y padx es el espacio que tiene el componente con su componente
# padre
# 
# padx aumenta el espacio vertical, arriba y abajo del componente
# pady aumenta el espacio horizontal, derecha e izquierda del componente#

#Otros cuadros

labelApellido = Label(frame, text="Apellido Paterno")
labelApellido.grid(row=1, column=0, pady=10)

entradaApellido = Entry(frame)
entradaApellido.grid(row = 1, column = 1, pady=10)
# En el caso que se quisiera mostrar otro digito al momento de 
# escribir en alguna de las entradas#

entradaApellido.config(show = "*")

root.mainloop()
