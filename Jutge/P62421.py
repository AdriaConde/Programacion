concatenar=""
palabra=input()
lista=palabra.split()
for recorrer in lista:
    concatenar=recorrer + " " + concatenar
    
print(concatenar[:-1])