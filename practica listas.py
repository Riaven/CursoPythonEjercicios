#A continuación se creará una lista para almacenar datos
# y posteriormente hacer un llamado a la lista completa, como
# a un solo dato por su índice#

miLista = ["Osiris", "Sylvia", 3.65, "Adriadna"]

#se agrega un nuevo elemento a lista al final#
miLista.append("Maritza")
#agrega en el índice que se le indique#
miLista.insert(0, False)
#agrega los elementos en la lista#
miLista.extend([5, "Fredy"])

#Se ponen dos puntos dentro de los corchetes para poder
# obtener todos los datos que contiene la lista llamada#
print(miLista[:])

#En el caso de querer obtener un dato en concreto de una lista
# al momento de imprimir, dentro de los corchetes se le pasa
# el índice del elemento en cuestión#
print(miLista[0])

#En el caso de solicitar un dato con un índice negativo, este
# comienza a contar desde el final de la lista y por lo tanto, 
# devuelve el dato correspondiente#
print(miLista[-1])#<- devuelve 'Adriadna', que es el último de la lista

#Cuando se quiere acceder a una porcion de la lista #
print(miLista[1:3])
#Esto incluye al índice 1, pero excluye al 3, por que 
# imprime los índices 1 y 2
# si omites el primero, entiende que es el índice 0
# print(miLista[:2] imprime el índice 1 y 2#


#para acceder a los últimos elementos de una lista
# desde el índice que se le indique hasta el final#
print(miLista[2:])

#para saber el índice de un elemeto, si hay dos igual
# siempre devuelve el primer elemento que encuentra#
print(miLista.index("Fredy"))

#para saber si un elemento existe dentro de una lista
# devuelve un true o false#
print("Marco" in miLista)

#para eliminar algún elemeto de una lista#
miLista.remove(5)

miSegundaLista = ["Iron Man", "Skrillex"]
sumaDelistas = miLista + miSegundaLista
print(sumaDelistas[:])