#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
num=0
num_secreto=0

num=int(input("Introduce el número secreto del 1 al 5: "))
while num<1 or num>5:
    num=int(input("El número secreto debe ser entre el 1 y el 5: "))
numero_secreto=random.randint(1, 5)


while num!=numero_secreto:
    print("Número no acertado")
    num=int(input("Vuelve a intentarlo: "))
    while num<1 or num>5:
        num=int(input("El número secreto debe ser entre el 1 y el 5: "))
else:
    print("Número acertado")