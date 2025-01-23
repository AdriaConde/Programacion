#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    inicio = num2
    fin = num1
else:
    inicio = num1
    fin = num2

pares = []
impares = []

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Números pares en el rango: {pares}")
print(f"Números impares en el rango: {impares}")
