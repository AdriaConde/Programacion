#22. 
var1=float(input("Dime una nota:"))

if var1<10 and var1>0:
        if var1<5.0:
            print(f"Has sacado un {var1}, has suspendido")
        if var1>=5.0:
            print(f"Has sacado un {var1}, has aprobado")
            
else:
   print("La nota está fuera de los límites establecidos")   