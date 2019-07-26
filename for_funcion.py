

def comprobar_email(letra):
    """Compruba que la letra pasada por parámetro sea un @

    Parámetros:
    letra (str): Letra a comprobar

    Retorna:
    int: 1 si se ha encontrado, 0 si no
    """
    correcto = 0
    if letra == "@":
        correcto+=1
    return correcto

email = False
miEmail = input("Introduce un Email a comprobar : ")
for i in miEmail:
    
    if(comprobar_email(i)==1):
        email=True

if email:
    print("Email es correcto")
else:
    print("Email incorrecto")