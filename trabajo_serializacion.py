import pickle
#Para poder guardar los datos en un archivo binario, se abre el archivo
# en wb = write binary

#lista_nombres = ["Pedro", "María", "Franco"]
#fichero_binario = open("lista_nombres", "wb")
#pickle.dump(lista_nombres, fichero_binario)
# fichero_binario.close()#


#Para poder cargar la información que contiene el archivo en binario
fichero = open("lista_nombres", "rb")
lista = pickle.load(fichero)
print(lista)