#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
num=0
numero_secreto=0
contador=0

num=int(input("Introduce el número secreto del 1 al 5: "))
contador +=1
while num<1 or num>5:
    num=int(input("El número secreto debe ser entre el 1 y el 5: "))
numero_secreto=random.randint(1, 5)

while num!=numero_secreto and contador<3:
    print("Número no acertado")
    contador +=1
    num=int(input("Vuelve a intentarlo: "))
    while num<1 or num>5:
        num=int(input("El número secreto debe ser entre el 1 y el 5: "))

if num!=numero_secreto:
    print("Has agotado los intentos")
else:
    print("Número acertado")