#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
var1=float(input("Introduce un valor:"))
var2=float(input("Introduce otro valor:"))
print("El coeficiente es:",round(var1/var2, 2))
print("El resto es:",round(var1%var2, 2))
if var1%2==0:
    print("El dividendo es par")
if not var1%2==0:
    print("El dividendo es impar")
