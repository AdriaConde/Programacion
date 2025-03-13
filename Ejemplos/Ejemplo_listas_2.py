#Ejemplo listas 2
frase=input("Introduce una frase: ")

lista=[]

lista=frase.split()

palabra=input("Introduce una palabra: ")

print(lista)
print(lista.count(palabra))

frasenueva="-".join(lista)

print(frasenueva)