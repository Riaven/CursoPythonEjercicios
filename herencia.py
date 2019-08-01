#Clase padre
class Vehiculo():
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__enMarcha = False
        self.__acelera = False
        self.__frena = False

    def arrancar(self):
        self.__acelera = True
    def acelerar (self):
        self.__acelera = True
    def frenar(self):
        self.__frena
    def estado(self):
        print("Marca :", self.__marca)
        print("Modelo :", self.__modelo)
        print("En marcha :", self.__enMarcha)
        print("Acelerando :", self.__acelera)
        print("Frenando :", self.__frena)
    
#Clase hija
# En los paréntesis que se encuentran
# al lado del nombre de la clase, va el
# nombre de la clase Padre
class Moto(Vehiculo):
    pass

motocicleta = Moto("Honda", "510")
motocicleta.estado()