# al poner en los parámetros un *, se le dice que puede recibir mas de un 
# parámetro y esto se guarda como tupla
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudadesDevueltas = devuelve_ciudades("Santiago", "Rancagua", "San Bernardo")
print(next(ciudadesDevueltas)) #llamarlo una vez devuelve Santiago
print(next(ciudadesDevueltas)) #llamarlo una vez devuelve Rancagua

