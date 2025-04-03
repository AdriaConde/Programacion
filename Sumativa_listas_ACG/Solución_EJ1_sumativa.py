milista=[]
milista1=[]
milista2=[]
numeros=""
maximo=0
minimo=0
promedio=0

numeros=input("Introduce 6 números separados por un guión: ")

milista=numeros.split("-")

milista1=[int(x) for x in milista]

maximo=max(milista1)
minimo=min(milista1)
promedio=round(sum(milista1)/len(milista1),4)

for recorrer in milista1:
    if recorrer>promedio:
        milista2.append(recorrer)

print(maximo)
print(minimo)
print(promedio)
print(milista2)