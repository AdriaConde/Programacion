#Juego ejemplo while
import random

num=int(input("Introduce el número secreto: "))
numero_secreto=random.randint(1, 10)

while num!=numero_secreto:
    print("no es igual")
    num=int(input("Vuelve a intentarlo: "))
else:
    print("very good")