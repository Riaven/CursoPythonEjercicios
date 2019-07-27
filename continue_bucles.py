# sirve para saltar el código que viene después de donde
# se declara la instrucción y pasa a la siguiente iteración

for letra in "Python":
    if letra == "h":
        continue
        #Salta lo que viene en el código cuando la letra es una h
    print("Viendo la letra " + letra)