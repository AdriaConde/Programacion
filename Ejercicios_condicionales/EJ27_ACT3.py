#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
var1=input("Dime una letra:")

if var1.islower()==True:
    print("La letra es minúscula")
elif var1.isupper()==True:
    print("La letra es mayúscula")
elif var1.isnumeric()==True:
    print("El valor introducido es un número") 
else:
    print("La letra es mayúscula ¿?")