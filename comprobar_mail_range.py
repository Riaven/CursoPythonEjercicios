valido = False
email = input("Introduce el email a comprobar : ")

for i in range(len(email)):
    if email[i]=="@":
        valido = True


if valido:
    print("El email está correcto")
else:
    print("Email incorrecto")

