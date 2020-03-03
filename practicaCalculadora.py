# Practica con una calculadora, para pobar las funciones de Tkinter#
from tkinter import *
root = Tk()
root.title("Calculadora") # nombre de la ventana
#Frame
frame = Frame(root)
frame.pack()

#------------Variables globales a utilizar
resultado = 0
operador = ""


#------------pantalla
numeroseleccionado = StringVar()
numeroseleccionado.set("")
pantalla = Entry(frame, textvariable = numeroseleccionado)
pantalla.grid(row = 1 , column = 1, pady = 10, padx = 10, columnspan = 4)
pantalla.config(bg = "black", fg="#03f943", justify = "right")


#---------funcionalidad de botones--------------
# funcion que imprime los numeros en la pantalla de acuerdo a lo seleccionado en los botones
def numero(num):
    global operador
    if(operador != ""): #comprueba que el operador es distinto de  vacío
        numeroseleccionado.set(num)#setea el numero de pantalla por el que se aprete 
       # operador = "" #se cambia el operador a vacio nuevamente
    else:
        numeroseleccionado.set(numeroseleccionado.get() + num) #como operador esta vacio, se concadena con el numero que se encuentra
  
##############variables para las operaciones 
num1 = 0
cantidad = 0
cantidadMulti = 0
cantidadDivi = 0
#################

# función que realiza la operación matemática solicitada
def operacion(num, simbolo):
    global operador
    global resultado
    global num1
    #para la suma
    if(simbolo == "+"):
        operador = "suma"
        resultado += int(num)
        numeroseleccionado.set(resultado)

    #para la resta#    
    if(simbolo == "-"):
        
        global cantidad
        operador = "resta"
        if(cantidad == 0): # referencia a la cantidad de numeros, si es 0, num1 tiene el primer numero
            num1 = int(num)
            resultado = num1
        else:
            if(cantidad == 1): # si ya hay un numero resultado sera la resta entre el num1 y el nuevo numero
                resultado = num1 - int(num)
            else:
                resultado = resultado - int(num) #de haber mas de un numero se le resta al resultado

            numeroseleccionado.set(resultado) #se muestra el resultado en pantalla
            resultado = int(numeroseleccionado.get()) #resultado tiene el numero que sale en pantalla

        cantidad +=1 #se aumenta la cantidad de numeros a 1
        



    #para la multiplicacion#
    if(simbolo == "x"):
        
        global cantidadMulti
        operador = "multiplica"
        if(cantidadMulti == 0): 
            num1 = int(num)
            resultado = num1
        else:
            if(cantidadMulti == 1): 
                resultado = num1 * int(num)
            else:
                resultado = resultado * int(num) 

            numeroseleccionado.set(resultado) 
            resultado = int(numeroseleccionado.get()) 

        cantidadMulti +=1 

    #para la division#
    if(simbolo == "/"):
        
        global cantidadDivi
        operador = "divide"
        if(cantidadDivi == 0):
            num1 = int(num)
            resultado = num1
        else:
            if(cantidadDivi == 1): 
                resultado = num1 / int(num)
            else:
                resultado = resultado / int(num) 

            numeroseleccionado.set(resultado) 
            resultado = int(numeroseleccionado.get())

        cantidadDivi +=1 


def igual():
    global resultado
    global operador
    global cantidad
    #para cada una de las operaciones
    if(operador == "suma"):
        numeroseleccionado.set(resultado + int(numeroseleccionado.get()))
        operador = ""
        resultado = 0
    elif(operador == "resta"):
        numeroseleccionado.set(resultado - int(numeroseleccionado.get()))
        operador = ""
        resultado = 0
        cantidad = 0
    elif(operador == "divide"):
        numeroseleccionado.set(resultado / int(numeroseleccionado.get()))
        operador = ""
        resultado = 0
        cantidadDivi = 0
    elif(operador == "multiplica"):
        numeroseleccionado.set(resultado * int(numeroseleccionado.get()))
        operador = ""
        resultado = 0
        cantidadMulti = 0
    
    

#función elimina el contenido de la pantalla
def borrarPantalla():
    numeroseleccionado.set("")
    operador = ""
    resultado = 0


#grafica##################################

#Botones 7 8 9 x
boton7 = Button(frame, text = "7", width = 3, command = lambda:numero("7"))
boton7.grid(row = 2, column = 1)
boton8 = Button(frame, text = "8", width = 3, command = lambda:numero("8"))
boton8.grid(row = 2, column = 2)
boton9 = Button(frame, text = "9", width = 3, command = lambda:numero("9"))
boton9.grid(row = 2, column = 3)
botonx = Button(frame, text = "x", width = 3, command = lambda:operacion(numeroseleccionado.get(), "x"))
botonx.grid(row = 2, column = 4)

#Botones 4 5 6 -
boton4 = Button(frame, text = "4", width = 3, command = lambda:numero("4"))
boton4.grid(row = 3, column = 1)
boton5 = Button(frame, text = "5", width = 3, command = lambda:numero("5"))
boton5.grid(row = 3, column = 2)
boton6 = Button(frame, text = "6", width = 3, command = lambda:numero("6"))
boton6.grid(row = 3, column = 3)
botonmenos = Button(frame, text = "-", width = 3, command = lambda:operacion(numeroseleccionado.get(), "-"))
botonmenos.grid(row = 3, column = 4)

#Botones 1 2 3 +
boton1 = Button(frame, text = "1", width = 3, command = lambda:numero("1"))
boton1.grid(row = 4, column = 1)
boton2 = Button(frame, text = "2", width = 3, command = lambda:numero("2"))
boton2.grid(row = 4, column = 2)
boton3 = Button(frame, text = "3", width = 3, command = lambda:numero("3"))
boton3.grid(row = 4, column = 3)
botonmas = Button(frame, text = "+", width = 3, command = lambda:operacion(numeroseleccionado.get(), "+"))
botonmas.grid(row = 4, column = 4)

#Botones C 0 / =
botonborrar = Button(frame, text = "C", width = 3, command = borrarPantalla)
botonborrar.grid(row = 5, column = 1)
boton0 = Button(frame, text = "0", width = 3, command = lambda:numero("0"))
boton0.grid(row = 5, column = 2)
botondiv = Button(frame, text = "/", width = 3, command = lambda:operacion(numeroseleccionado.get(), "/"))
botondiv.grid(row = 5, column = 3)
botonigual = Button(frame, text = "=", width = 3, command = lambda:igual())
botonigual.grid(row = 5, column = 4)


root.mainloop()
