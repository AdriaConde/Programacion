#Ejercicio2
var_suma_pos=0
var_suma_neg=0

for contador in range (0,6):
    var1=int(input("Introduce un valor: "))
    if var1>0:
        var_suma_pos=var_suma_pos+var1
    
    if var1<0:
        var_suma_neg=var_suma_neg+var1

print(f"Suma de números positivos: {var_suma_pos}")
print(f"Suma de números negativos: {var_suma_neg}")