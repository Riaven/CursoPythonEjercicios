from tkinter import *

# Para poder abrir una ventana
raiz=Tk()
#Titulo de la ventana
raiz.title("Ventana")
#no permite cambiar el tamño de la ventana
raiz.resizable(1,0) #width, heigth ---- permite boolean
#Para poder cambiar el ícono de la ventana, se debe de utilizar una imagen .ico
raiz.iconbitmap("gato.ico")

#Ancho y alto de la ventana
raiz.geometry("450x500")

raiz.config(bg="green")


# La ventana pra permanecer abierta, debe de estar a la escucha de cualquier eventro
# eso se logra con el método mainloop(), permanece en un loop infinito
#Siempre este método debe de ir al último del todo el código
raiz.mainloop()
