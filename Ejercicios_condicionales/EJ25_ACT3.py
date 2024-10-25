#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10 Utilizar elif sin operadores lógicos.
var1=float(input("Dime una nota:"))

if var1<10 and var1>0:
        if var1>5.0 and var1<6.5:
            print(f"Has sacado un {var1}, has sacado un satisfacorio")
        if var1>=6.5 and var1<8.5:
            print(f"Has sacado un {var1}, has sacado un notable")
        if var1>=8.5 and var1<10:
            print(f"Has sacado un {var1}, has sacado un excelente")
        if var1<=5.0:
            print(f"Has sacado un {var1}, has sacado un insuficiente")
            
else:
   print("La nota está fuera de los límites establecidos") 