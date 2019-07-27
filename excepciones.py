# Suma
def suma(num1, num2):
    return num1+num2
# Resta
def resta(num1, num2):
    return num1-num2
# Multipliación
def multiplicacion(num1, num2):
    return num1*num2
# División
def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No es posible realizar una división por cero :(")
        return "Error en la operación"

print("Calculadora básica")
while True:
    try:
        numero1 = int(input("Introduce el primer número "))
        numero2 = int(input("Introduce el segundo número "))
        break
    except ValueError:
        print("Valores incorrectos, intenta otra vez")
# Operación
op = int(input("Introduce \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n "))
if op == 1:
    print("La suma es " + str(suma(numero1, numero2)))
elif op == 2:   
    print("La resta es " + str(resta(numero1, numero2)))
elif op == 3:   
    print("La multipliación es " + str(multiplicacion(numero1, numero2)))
elif op == 4:   
    print("La división es " + str(division(numero1, numero2)))
else:
    print("Operación errónea")

print("Operación terminada")