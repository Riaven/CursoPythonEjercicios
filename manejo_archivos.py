from io import open
# para poder escribir en un archivo de texto
archivo_texto = open("miArchivo.txt", "w")
frase = "Frase para escribir en el archivo .txt \n desde un programa python"
archivo_texto.write(frase)
archivo_texto.close()
print("Aquí se ha escrito en el archivo")

# para poder abrir un archivo de texto y rescatar su contenido
archivo_texto = open("miArchivo.txt", "r") # read
# le otorga a la variable .texto. el contenido del archivo que se abrió en modo lectura anteriormente
texto = archivo_texto.read() 
#Siempre una vez utilizado el archivo, se debe de cerrar, para no ocupar memoria
archivo_texto.close()
print("Se ha leído desde el archivo")
print(texto) # imprime lo que se almacenó en la variable
