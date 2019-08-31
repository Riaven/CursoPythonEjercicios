from io import open

archivo_texto = open("miArchivo.txt", "w")
frase = "Frase para escribir en el archivo .txt \n desde un programa python"
archivo_texto.write(frase)
archivo_texto.close()