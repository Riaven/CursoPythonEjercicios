from io import open
archivo_texto = open("ArchivitoPuntero.txt", "r+")
lista_lineas = archivo_texto.readlines() #Leemos y obtenemos las lineas
lista_lineas[0] = "Estamos creando un archivo " #Cambiamos la linea 
archivo_texto.seek(0) #Devuelve al punto inicial
archivo_texto.writelines(lista_lineas)
archivo_texto.close()