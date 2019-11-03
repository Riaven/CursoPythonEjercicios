from tkinter import *

# Para poder abrir una ventana
raiz=Tk()
#Titulo de la ventana
raiz.title("Ventana")
#no permite cambiar el tamño de la ventana
#raiz.resizable(1,0) #width, heigth ---- permite boolean
#Para poder cambiar el ícono de la ventana, se debe de utilizar una imagen .ico
raiz.iconbitmap("gato.ico")

#Ancho y alto de la ventana
#La raiz siempre se va a adaptar a su contenedor interno, darle tamaño a la raiz no es válido
#raiz.geometry("450x500")
#Cambia el color del fondo de la ventana
raiz.config(bg="green")

#Crear un Frame
miFrame = Frame()
#empequeta el frame dentro de la ventana
#side permite = left, right, top, bottom
#anchor permite = n , s, w, e <-- puntos cardinales
#fill efecto de rellenado

miFrame.pack()
#Le da un color al frame
miFrame.config(bg="blue")
miFrame.config(width = "650", height = "350")

#Tamaño del borde del frame
miFrame.config(bd=35)
#Tipo de borde
miFrame.config(relief= "groove")


#Para cambiar cursor

miFrame.config(cursor="pirate")
# La ventana pra permanecer abierta, debe de estar a la escucha de cualquier eventro
# eso se logra con el método mainloop(), permanece en un loop infinito
#Siempre este método debe de ir al último del todo el código
raiz.mainloop()
