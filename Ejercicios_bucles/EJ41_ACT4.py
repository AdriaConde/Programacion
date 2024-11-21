#41. Imprime el siguiente patrón utilizando for:
secuencia="54321"
print(secuencia)
for contador in range(len(secuencia)-1):
    nueva_secuencia=secuencia[1:]
    print(nueva_secuencia)
    secuencia=nueva_secuencia
