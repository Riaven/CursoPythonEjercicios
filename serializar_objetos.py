import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enMarcha = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca : ", self.marca)
        print("Modelo : ", self.modelo)
        print("En marcha : ", self.enMarcha)
        print("Acelera : ", self.acelera)
        print("Frena : ", self.frena)

coche1 =  Vehiculo("Mazda", "MX5")
coche2 =  Vehiculo("Seat", "Leon")
coche3 =  Vehiculo("Renault", "Menage")

coches_lista = [coche1, coche2, coche3]

fichero_coches = open("lista_coches", "wb")
pickle.dump(coches_lista, fichero_coches)
fichero_coches.close()

#Borrado de fichero
del(fichero_coches)

#Abrir fichero binario de objetos
fichero = open("lista_coches", "rb")
lista_coche = pickle.load(fichero)
fichero.close()
for coche in lista_coche:
    print(coche.estado())
