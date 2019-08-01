class Auto():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 100
        self.__ruedas =  4
        self.__estado = True # True para en buen estado, False, para mal estado
    # Recibe y notifica el estado del auto
    def revisionEstado(self, estadoAuto):
        self.__estado = estadoAuto
        if self.__estado:
            chequeo = self.chequeo_interno()
        if self.__estado and chequeo:
            return "El auto se encuentra en buen estado"
        elif(self.__estado and chequeo == False):
            return "Problemas con el chequeo"
        else:
            return "El aunto NO se encuentra en buen estado"
    # Devuelve todos los atributos del auto
    def entregaInfo(self):
        print("La dimesion de chasis :" , self.__anchoChasis , "x", self.__largoChasis)
        print("Ruedas :", self.__ruedas)
        print("Estado del auto : " , self.__estado)

    def chequeo_interno(self):
        print("Chequeo interno")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "Cerradas"
        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False

autito =  Auto()
autito.entregaInfo()
print(autito.revisionEstado(True))
autito.entregaInfo()
