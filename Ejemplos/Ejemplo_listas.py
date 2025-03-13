#Ejemplo listas
milista=[]
total=0
total_1=0
listamultiplicar=[]

numero=int(input("Introduce un número: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número o 0 para acabar: "))
    
print(milista)
print(max(milista))
print(min(milista))

for recorrer in milista:
    total=total+recorrer 
print(total)

for recorrer in range(0, len(milista)):
    total_1=total_1 + milista[recorrer]
print(total_1)

print(sum(milista))

for recorrer in milista:
    multi=recorrer*2
    listamultiplicar.append(multi)
    
print(f"lista multiplicada {listamultiplicar}")