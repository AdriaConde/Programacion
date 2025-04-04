#Ej.4
#Antes de comenar he estado probando directamente en la consola cuales podian ser las operaciones y he descubierto que eran //, ** y %
#Mismo código para pedir algo por pantalla y con int porque en el ejemplo no salen decimales
var1=int(input("Introduce un número:"))
var2=int(input("Introduce otro número:"))
#Estas tres lineas siguientes son iguales solo cambiando el operador y el nombre del operador dentro de las comillas de texto. He printeado con formato y he escrito el tipo de operación que es
print(f"El resultado de la división entera de {var1} y {var2} es:", var1//var2)
print(f"El resultado de la potencia de {var1} y {var2} es:", var1**var2)
print(f"El resultado del módulo de {var1} y {var2} es:", var1%var2) 
