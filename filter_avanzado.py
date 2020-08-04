# Utilizaremos la función filter, para determinar los empleados que tengan 
# cierto rango de salario#
class Empleado():
    # Constructor
    def __init__(self, nombre,cargo, salario):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo
    # Devolvemos la info
    def __str__(self):
        return "El trabajador {} se desempeña como {} con un salario total de {} pesos".format(
            self.nombre,
            self.cargo,
            self.salario
        )


lista_empleados = [
    Empleado('Osiris', 'Mesera', 120000),
    Empleado('Maria', 'Ingeniera Financiera', 350000),
    Empleado('Edison', 'Informático', 400000),
    Empleado('Luis', 'Asistente', 140000),
    Empleado('Francisca', 'Informática', 500000)
]

salarios_altos = list(filter(lambda empleado: empleado.salario >= 350000, lista_empleados))

for salarios in salarios_altos:
    print(salarios)