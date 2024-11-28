#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
palabra = input("Introduce una palabra: ")

vocales = []
consonantes = []

for letra in palabra:
    if letra in 'aeiouáéíóú':
        vocales.append(letra)
    elif letra:
        consonantes.append(letra)

print("Vocales:", vocales)
print("Consonantes:", consonantes)