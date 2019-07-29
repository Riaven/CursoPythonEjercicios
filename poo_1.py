# Clase de tipo coche
class Coche():
    #Atributos
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    # Método 
    def arrancar(self):
        self.enMarcha = True
    
    def devuelveEstado(self):
        if self.enMarcha:
            return "Coche funcionando"
        else: 
            return "Coche en mal estado"

# para crear una instancia de clase coche
micoche = Coche()
micoche.largoChasis = 300

print("Las características de mi coche son: ")
print(" Chasis :" , micoche.largoChasis , "x" , micoche.anchoChasis)
print(" Ruedas : ", micoche.ruedas)
micoche.arrancar()
print(" Funcional : ", micoche.enMarcha)

miHiundai = Coche()
# se llama al método correspondiente
print(miHiundai.devuelveEstado())
