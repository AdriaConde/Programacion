#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
num=0
numero_secreto=0
contador=0

num=int(input("Introduce el número secreto entre 0 y el 1000: "))
contador +=1
numero_secreto=random.randint(1, 1000)

while num!=numero_secreto:
    if numero_secreto<num:
        print("El número que has introducido es menor.")
    else:
        print("El número que has introducido es mayor.")
    num=int(input("Introduce el número secreto entre 0 y el 1000: "))
    contador +=1

else:
    print(f"Número acertado, en {contador} intentos.")