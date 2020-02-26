from tkinter import * #importa todo lo de la libreria tkinter
root = Tk() #crea la instancia
miFrame =  Frame(root, width= 500, height = 400) #crea el frame con la instancia y el ancho y alto
miFrame.pack()## empaqueta el frame

miLabel = Label(miFrame, text = "Hola esto es un ejemplo")
#Para que respete el tamaño de la ventana dada anteriormente
# se debe de llamar al método place en lugar de pack
# ya que place posiciona el label dentro del frame sin cambiar su 
# tamaño, ya que pack ajusta la venana a las dimensiones del label ..
# dentro del método place se debe de establecer la posición que tomará
# el label dentro del frame, se debe de pasar x e y con los datos#
miLabel.place(x =1, y =1)
#para poder usar imagenes dentro de un label
imagen = PhotoImage(file="error.png")
Label(miFrame, image = imagen).place(x = 20, y = 50)
root.mainloop() ## llama al metodo para que se active la ventana