from io import open
archivo_texto = open("miArchivo.txt", "r")
print(archivo_texto.read())
#Los primeros 7 caracteres no los toma en cuenta 
#archivo_texto.seek(7) 
archivo_texto.seek(0)

#En el caso de querer justo la mitad del archivo
archivo_texto.seek(len(archivo_texto.read())/2)

#Vuelve a imprimir, pero desde donde quedó el puntero,
# que es la posición 8
#print(archivo_texto.read(11))

print(archivo_texto.read())