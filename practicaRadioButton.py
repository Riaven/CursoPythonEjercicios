from tkinter import *
root = Tk()
#uso de radio button
# solo con definirlos y darles un texto, por defecto vienen todos seleccionados y sin posibilidad
# de ser seleccionados o deseleccionados con el raton#
varOpcion = IntVar()

# Función para saber cual de las dos opciones han sido seleccionadas en el momento#
def imprimir():
    if (varOpcion.get() == 1):
        info.config(text = "Eres de género femenino")
    else:
        info.config(text = "Eres de género masculino")

Label(text = "Seleccione género").pack()
Radiobutton(root, text="Femenino", variable = varOpcion, value = 1, command = imprimir).pack()
Radiobutton(root, text="Masculino", variable = varOpcion, value = 2, command = imprimir).pack()
info = Label(root) # si es que se empaqueta de inmediato, la variable info, almacena nulo
info.pack() # ya que pack es un método
print(varOpcion.get())

root.mainloop()