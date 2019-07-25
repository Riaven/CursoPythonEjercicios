# Creación de un diccionario, los elementos de este
# van dentro de llaves '{}' 

# Alemania = clave, Berlín = valor
miDiccionario = {"Alemania" : "Berlín", "Francia" : "París", "Reino Unido" : "Londres"}
# Para llamar a un elemento en concreto, al imprimir por
# ejemplo, se busca por la clave#
print(miDiccionario["Alemania"])

#Agregar elemento 
miDiccionario["Chile"] = "Santa Lucía"

print(miDiccionario)
# Se otorga el valor de referencia
miDiccionario["Chile"] = "Santiago"
print(miDiccionario)

# Eliminar
del(miDiccionario["Reino Unido"])
print(miDiccionario)

# Diccionario con tupla
tupla = ["Franco ", 5, False]
diccionarioTupla = {"Iron" : "Man", 3 : tupla}
print(diccionarioTupla)
# Devuelve las claves del diccionario
print(diccionarioTupla.keys())
#devuelve los valores del diccionario
print(diccionarioTupla.values())
#largo del diccionario
print(len(diccionarioTupla))