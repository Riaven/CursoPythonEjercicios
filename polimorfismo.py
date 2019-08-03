class Coche():
    def desplazamiento(self):
        print("Me desplazo en cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo en dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo en seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

desplazamientoVehiculo(Moto())
