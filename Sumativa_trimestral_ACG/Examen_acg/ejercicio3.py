#Ejercicio3
var_cifras=int(input("Introduce un número de cifras: "))
var_num=input("Introduce un número con esas cifras: ")
var_suma=0

if len(var_num)==var_cifras:
    for contador in range(var_cifras):
        var_suma=var_suma+int(var_num[contador])
    
    print("Resultado: ", var_suma)

else:
    print("Error, no coincide el número de cifras")    