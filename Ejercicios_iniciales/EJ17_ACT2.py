#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
var1=float(input("Introduce tu peso en Kg:"))
var2=float(input("Introduce tu estatura en metros:"))
var_IMC=var1/(var2**2)
print(f"Si pesas {var1} y mides {var2}, tu IMC es:", round(var_IMC,2))
if var_IMC>=25:
    print("Hay sobrepeso")
