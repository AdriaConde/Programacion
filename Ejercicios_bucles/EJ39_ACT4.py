#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
n_numeros=int(input("Introduce la cantidad de números que deseas introducir: "))
positivo=0
negativo=0
ceros=0

for contador in range(n_numeros):
    num=float(input("Introduce un número: "))
    if num>0:
        positivo=positivo+1
    if num<0:
        negativo=negativo+1
    if num==0:
        ceros=ceros+1

print(f"La cantidad de números positivos es {postivo}")
print(f"La cantidad de números negativos es {negativo}")
print(f"La cantidad de ceros es {ceros}")