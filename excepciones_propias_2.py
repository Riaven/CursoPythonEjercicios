import math
def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
#Se realiza el casteo a int 
op1 = int(input("Introduce un número : "))
try:
    print(calculaRaiz(op1))

# Se le da un alias al error para poder utilizarlo
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
print("Programa finalizado")