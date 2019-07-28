def divide():
    while True:
        try:
            op1 = float(input("Introduce el primer múmero "))
            op2 = float(input("Introduce el segundo múmero "))
            print("División : " + str(op1/op2))
            break
        except ZeroDivisionError:
            print("No se puede dividir por 0")
        except ValueError:
            print("El valor ingresado no es válido")
        finally:
            print("Finalizado")


divide()