print("Practica de funcionalidad de condicional IN")
opcion = input("Escribe una letra a, b o c")
letra = opcion.upper();
if letra in ("A", "B", "C"):
    print("Correcto!")
else:
    print("Incorrecto :(")