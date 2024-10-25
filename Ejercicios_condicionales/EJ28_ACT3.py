#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
var1=input("Dime una letra:")

if var1.islower()==True:
    print("La letra es minúscula")
elif var1.isupper()==True:
    print("La letra es mayúscula")
elif var1.isnumeric()==True:
    print("El valor introducido es un número") 
elif var1.isalnum()==False:
    print("El valor introducido es un símbolo")