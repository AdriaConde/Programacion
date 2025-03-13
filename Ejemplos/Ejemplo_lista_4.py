#Ejemplo listas 4
lista1=[]
lista2=[]
lista3=[]

valores=input("Introduce valores separados por un guión: ")

lista1=valores.split("-")

print(lista1)

for recorrer in lista1:
    if recorrer.isnumeric():
        lista2.append(recorrer)
    else:
        lista3.append(recorrer)
        
print(lista1)
print(lista2)
print(lista3)