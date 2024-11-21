#40. Crea un programa que cuente todos los números pares hasta el número 50
var_par=0
var_impar=0
for contador in range(0,50,2):
    var_par=var_par+1

for contador in range(1,50,2):
    var_impar=var_impar+1
    
print(f"El total de pares es: {var_par}")
print(f"El total de impares es: {var_impar}")
