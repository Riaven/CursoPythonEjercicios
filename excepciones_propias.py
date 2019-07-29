def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("Edad menor que 0")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres adulto"
    elif edad < 100:
        return "Eres adulto mayor"

print(evaluaEdad(-9))