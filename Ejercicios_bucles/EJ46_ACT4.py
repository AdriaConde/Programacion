#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra = input("Introduce una palabra: ")

vocales = []
consonantes = []

for letra in palabra:
    if letra.lower() in 'aeiouáéíóú':
        vocales.append(letra)
    elif letra.isalpha():
        consonantes.append(letra)

print("Vocales:", vocales)
print("Consonantes:", consonantes)