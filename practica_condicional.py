print("Programa Becas 2019")
distaciaEscuela = int(input("Distancia domicilio a Escuela "))
hermanosCantidad =  int(input("Cantidad de hermanos "))
salarioFamiliar = int(input("Salario total Familiar "))

if distaciaEscuela > 40 and hermanosCantidad > 2 or salarioFamiliar <= 20000:
    print("Eres becado")
else:
    print("No cumples con los requisitos mínimos")