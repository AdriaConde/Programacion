#Ej.2
#Para las dos primeras líneas he escrito el mismo código tan solo he cambiado el nombre de las variables y el mensaje. He escrito float porque en el ejemplo nos daban numeros decimales. Y el input lo he puesto para que preguntar por pantalla
var1=float(input("Introduce el primer número:"))
var2=float(input("Introduce el segundo número:"))
#He escrito la operación que pedia el ejercicio en este caso suma
var_total=var1+var2
#He printeado con formato el resultado de la suma, con las variables entre llaves, como pide el enunciado
print(f"El resultado de sumar {var1} y {var2} es:", var_total)
#ídem que en la línea anterior, lo único que he convertido var_total en entero, ya que en el ejemplo aparece sin decimales, por último he redondeado con el método round, 3 decimales como aparece en el código (,3)
print(f"El resultado de dividir {int(var_total)} y 3 es:", round(var_total/3,3))
