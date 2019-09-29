import pickle
#Se crea la clase persona
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se ha creado ", self.nombre)
    
    #Permite obtener la información del objeto de la clase en un String
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
# Se crea una clase listaPersonas, para poder abrir un fichero externo y
# en el guardar la información correspondiente a las personas
class ListaPersonas():
    personas=[]
    def __init__(self):
        #Abre el fichero externo
        listaDePersonas = open("listafichero", "ab+")
        listaDePersonas.seek(0) #Pone el cursor al comienzo del fichero
        try:
            #trata de abrir y cargar el fichero si es que tuviera información dentro del mismo
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas".format(len(self.personas)))
        except:
            #En el caso de que el fichero se encontrara vacio
            print("El fichero se encuentra vacío")
        finally:
            # Siempre cerrará el archivo y eliminara la instancia creada
            listaDePersonas.close()
            del(listaDePersonas)
    #Se agrega una nueva persona
    def agregarPersonas(self, persona):
        self.personas.append(persona) # agrega al final
        self.guardarPersonasFichero()
    #Muestra a las personas
    def mostrarPersonas(self):
        for perso in self.personas:
            print(perso)
    #Se encarga de abrir el fichero en modo escritura binaria
    def guardarPersonasFichero(self):
        ListaPersonas = open("listafichero", "wb")
        pickle.dump(self.personas, ListaPersonas)
        del(ListaPersonas)
        #muestra la info del fichero externo
    def mostrarInfoFicheroExterno(self):
        print("La info del fichero externo es la siguiente :")
        listadePersonas = open("listafichero", "rb")
        listaExterna = pickle.load(listadePersonas)
        for listaE in listaExterna:
            print(listaE)
        
miLista = ListaPersonas()
#persona1 = Persona("María", "Femenino", 23)
#miLista.agregarPersonas(persona1)
#persona2 = Persona("Francisca", "Femenino", 21)
#miLista.agregarPersonas(persona2)
#persona3 = Persona("Osiris", "Femenino", 22)
#miLista.agregarPersonas(persona3)
#persona4 = Persona("Dante", "Masculino", 25)
#miLista.agregarPersonas(persona4)
#persona5 = Persona("Luis", "Masculino", 21)
#miLista.agregarPersonas(persona5)

miLista.mostrarInfoFicheroExterno()