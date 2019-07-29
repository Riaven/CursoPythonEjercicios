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
            return "El auto se encuentra en buen estado"
        else:
            return "El aunto NO se encuentra en buen estado"
    # Devuelve todos los atributos del auto
    def entregaInfo(self):
        print("La dimesion de chasis :" , self.__anchoChasis , "x", self.__largoChasis)
        print("Ruedas :", self.__ruedas)
        print("Estado del auto : " , self.__estado)

autito =  Auto()
autito.entregaInfo()
print(autito.revisionEstado(False))
autito.entregaInfo()
print(autito)