#42. Imprima el siguiente patrón con el ciclo for. 
secuencia="*****"
for contador in range(len(secuencia)):
    contador+=1
    print(secuencia[0:contador])

for contador in range(len(secuencia)):
    nueva_secuencia=secuencia[1:]
    print(nueva_secuencia)
    secuencia=nueva_secuencia