#Ejemplo while

contador=1
#Variable que cuenta pares
conta_pares=0

while contador<=20:
    if contador%2==0:
        conta_pares +=1

    contador +=1
print(f"Total de pares: {conta_pares}")