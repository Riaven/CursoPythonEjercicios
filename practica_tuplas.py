# A continuación se crea una tupla, se caracteriza por ser similar a las 
# listas pero no se pueden modificar, agregar, eliminar o modificar, 
# además se caracterizan por que los elementos deben de ser descritos dentro
# de paréntesis#
miTupla = ("Franco", 5)

# A continuación se crea una lista, la cual se recibe un tupla, convertida 
# a lista con el método list()#

miLista = list(miTupla)
print(miLista)

# A continuacion se crea una lista para posteriormente, convertila a tupla
# y pasarla a una misma#
lista = ["Sylvia", False, 5]
tupla = tuple(lista)

print(tupla)
# Ver si existe un elemento en la tupla
print(tupla.count(5))

# Para imprimir la longitud de la tupla se utiliza el método len()
print(len(tupla))
# Tupla unitaria
tuplaUnitaria = ("Sylvia",)# Sin la coma no es unitaria

# Desempaquetamiento de una tupla
nombre, edad = miTupla # Solo posee dos elementos
print(nombre) # Imprime el índice 0
print(edad) # Imprime el índice 1