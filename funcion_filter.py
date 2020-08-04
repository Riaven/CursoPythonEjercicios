# archivo de prueba para, ver el funcionamiento de la función filter

# Definición
# Verifica que los elementos de una secuencia cumplen una condición, 
# devolviendo un iterador con los elementos que cumplen dicha función #

#una lista de números pares e impares
numeros = [ 12, 7, 8, 78, 93, 4521, 47, 36, 85, 79, 100, 56]

# imprimimos la función, le pasamos por parámetro, la función que evaluará los datos
# como segundo parámetro pasamos el iterable, es decir, la lista, parseamos a una lista
# para que el resultado sea visible y no muestre la posición en memoria del resultado #
print(list(filter(lambda num :  num % 2 == 0 , numeros)))

