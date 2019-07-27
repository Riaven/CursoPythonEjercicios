# else en los bucles funciona cuando ya no queda nada por iterar

email = input("Introduce un email ")
for letra in email:
    if letra == "@":
        arroba = True
        break
else:
    arroba=False

print(arroba)