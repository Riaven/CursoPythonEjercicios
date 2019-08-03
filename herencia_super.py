class Persona():
    def __init__(self, nombre, edad, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
    def descripcion(self):
        print("Nombre :", self.__nombre)
        print("Edad :", self.__edad)
        print("Dirección :", self.__direccion)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, direccion):
        super().__init__(nombre, edad, direccion)
        self.__salario = salario
        self.__antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion();
        print("Salario : ", self.__salario)
        print("Antiguedad :", self.__antiguedad)


trabajador = Empleado(140, 12, "Juan", 35, "Sin info")
trabajador.descripcion()

persona = Persona("Franco", 5, "San Fernando")
print("-----")
persona.descripcion()

print(" Comprobando instancia de ")

print(isinstance(trabajador, Empleado)) # debe de dar True
print(isinstance(trabajador, Persona)) # Debe de dar True ya que hereda de Persona
print(isinstance(persona, Persona)) # True 
print(isinstance(persona, Empleado)) # False ya que no hereda y no tiene una conexión