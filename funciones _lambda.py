# Ejercicios para practicar lambda, son como las funciones anónimas que posee Javascript#
# Esto sería una función normal
def funcion(base, altura):
    return (base*altura)/2
#Usando la función anterior
print(funcion(23, 3))

area_triangulo = lambda base, altura : (base*altura)/2
print(area_triangulo(23,3))

#llamadas de igual manera como on demand, on line son funciones que usualmente 
# si fueran funciones normales, solo usarían una línea de código#