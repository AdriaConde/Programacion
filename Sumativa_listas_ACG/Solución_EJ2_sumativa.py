frase2=""
frase=input("Introduce la frase: ")
milista1=frase.split()
palabra=input("Introduce la palabra que quieres encontrar: ")
contar=milista1.count(palabra)

frase2=",".join(lista1)

print(contar)
print(frase2)