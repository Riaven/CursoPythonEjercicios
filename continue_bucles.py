# sirve para saltar el código que viene después de donde
# se declara la instrucción y pasa a la siguiente iteración

for letra in "Python":
    if letra == "h":
        continue
    print("Viendo la letra " + letra)