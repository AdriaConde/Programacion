#19. Programa que introduzca 2 números y devuelva cuál de los 2 es mayor, menor o son iguales:
var1=int(input("Dime un número:"))
var2=int(input("Dime un segundo número:"))

if var1<var2:
    print(f"El número {var2} es mayor que el número {var1}")
if var1>var2:
    print(f"El número {var1} es mayor que el número {var2}")
if var1==var2:
    print(f"El número {var1} es igual que el número {var2}")