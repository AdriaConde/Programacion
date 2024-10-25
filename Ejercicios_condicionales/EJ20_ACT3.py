#20. A partir del ejercicio anterior, forzar que el ususario solo pueda introducir por teclado números del 0-10
var1=int(input("Dime un número:"))
var2=int(input("Dime un segundo número:"))

if var1>10 and var1<0 or var2>10 and var2<0:
        if var1<var2:
            print(f"El número {var2} es mayor que el número {var1}")
        if var1>var2:
            print(f"El número {var1} es mayor que el número {var2}")
        if var1==var2:
            print(f"El número {var1} es igual que el número {var2}")
else:
   print("Uno de los dos números están fuera de los límites establecidos")   