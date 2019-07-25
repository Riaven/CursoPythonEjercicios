# Mensaje que muestra en consola
print("Programa de evaluación de notas de alumnos")
# Recibe lo escrito por el user en consola
notaAlumno = input("Introduce la nota: ")
# Función recibe la nota
def evaluacion (nota):
    valoracion = 5
    mensaje = "Aprobaste"
    if nota < valoracion:
        mensaje = "Estás desaprobado"
    else:
        mensaje = "Quién sabe"
    return mensaje
# Imprime la función anterior
print(evaluacion(int(notaAlumno)))