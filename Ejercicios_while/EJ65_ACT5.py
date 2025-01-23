#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time

lanzamientos = []

tiempo_inicio = time.time()

while True:
    dado = random.randint(1, 6)
    lanzamientos.append(dado)
    
    if time.time() - tiempo_inicio >= 3:
        break

print(f"Lanzamientos durante 3 segundos: {lanzamientos}")
print(f"Número total de lanzamientos: {len(lanzamientos)}")
