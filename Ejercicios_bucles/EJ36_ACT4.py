#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
suma=0
veces=int(input("Cuántos números naturales quieres sumar? "))

for contador in range(veces+1):
    suma=suma+contador

print(suma)