#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el númerode veces que se repite cada número.
import random

conteo = {i: 0 for i in range(1, 7)}

for _ in range(100):
    resultado = random.randint(1, 6)
    conteo[resultado] += 1

print("Resultados de las tiradas del dado:")
for numero, cantidad in conteo.items():
    print(f"Número {numero}: {cantidad} veces")

