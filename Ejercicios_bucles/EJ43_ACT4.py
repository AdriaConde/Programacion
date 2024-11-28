#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra.
palabra=input("Dime una palabra: ")
contar=0

for contador in range(len(palabra)):
    print("En la posición", contar, "está la", palabra[contar])
    contar+=1 