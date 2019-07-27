import math
print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número "))

intentos = 0

while numero < 0:
    intentos+=1    
    if intentos == 2:
        print("Demasiados intentos erróneos")
        break
    print("No se puede hallar la raíz de un número negativo")
    numero = int(input("Introduce un número "))

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
  