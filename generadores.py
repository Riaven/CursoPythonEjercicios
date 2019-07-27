def generaPares(limite):
    num = 1
   
    while num<limite:
        yield num*2
        num+=1
   
devuelvePares = generaPares(35)
#cada vez que se llama devuelve el elemento siguiente
print(next(devuelvePares))
print(next(devuelvePares))