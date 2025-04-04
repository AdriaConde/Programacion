#Ej.1
#He añadido float para que el valor que introduzca sea tratado como número con decimales
var_1=float(input("Introduce el primer número:"))
#He añadido comillas para que "Introduce el segundo número" sea texto, además he añadido float al igual que en la primera línea
var_2=float(input("Introduce el segundo número:"))
#He corregido el nombre de las variables ya que estaban guardadas como var_1 y var_2 no como var1 y var2, también he renombrado var total como var_total, porque no deben haber espacios en el nombre de las variables
var_total=var_1+var_2
#He quitado la coma luego de la f, he puesto llaves en lugar de paréntesis y he colocado una coma luego de cerrar comillas, por último he renombrado total como var_total ya que estaba guardada como tal.
print(f"El resultado de sumar {var_1} y {var_2} es:",var_total)
