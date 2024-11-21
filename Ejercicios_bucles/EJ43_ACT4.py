#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra.
palabra=input("Dime una palabra: ")
contar=0

for contador in range(len(palabra)):
    print(contador)
    contar+=1
print(contar)