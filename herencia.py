#Clase padre
class Vehiculo():
    #Método constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
        

    def arrancar(self):
        self.acelera = True
    def acelerar (self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca :", self.marca)
        print("Modelo :", self.modelo)
        print("En marcha :", self.enMarcha)
        print("Acelerando :", self.acelera)
        print("Frenando :", self.frena)
    
#Clase hija
# En los paréntesis que se encuentran
# al lado del nombre de la clase, va el
# nombre de la clase Padre
class Moto(Vehiculo):
    __levantaRueda=""
    def levantar(self):
        self.__levantaRueda = "Voy levantando la rueda delantera :O"
    # Sobreescritura de método, tiene que recibir la misma 
    # cantidad de parámetros que recibe el método padre
    # y a su vez tener el mismo nombre    
    def estado(self):
        print("Marca :", self.marca)
        print("Modelo :", self.modelo)
        print("En marcha :", self.enMarcha)
        print("Acelerando :", self.acelera)
        print("Frenando :", self.frena)
        print("Levantando la rueda delantera")

class Furgoneta(Vehiculo):
    def carga(self, carga):
        self.__carga =  carga
        if(self.__carga):
            print("La furgoneta se encuentra cargada")
        else:
            print("La furgoneta NO está cargada")

# Vehiculo eléctrico
class VElectrico():
    def __init__ (self):
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

# Bicicleta elétrica herencia multiple, para hacer uso
# de la herencia multiple, se debe de poner las clases
# padre dentro de los paréntesis, al momento de instanciar la clase
# y querer usar un método constructor, se dará prioridad
# al contructor de la clase, más cercana del nombre de la clase
# en este caso VElectrico 
class BicicletaElectrica(VElectrico, Vehiculo):
    pass

# Llamada de las clases para instanciarlas
motocicleta = Moto("Honda", "510")
motocicleta.estado()
#Furgoneta
print(" ")
furgon = Furgoneta("Mercedes Benz", "Modelo")
furgon.estado()
furgon.carga(True)
furgon.estado

print(" ")
#Bici
bici = BicicletaElectrica()
bici.cargarEnergia()