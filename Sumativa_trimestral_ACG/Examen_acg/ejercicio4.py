#Ejercicio4
var_min=int(input("Introduce el valor más bajo: "))
var_max=int(input("Introduce el valor más alto: "))
var_intervalo=int(input("Introduce intervalo: "))

for contador in range(var_min, var_max+1, var_intervalo):
    print(contador, end=" , ")