#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math

var_a=int(input("Introduce el primer término: "))
var_b=int(input("Introduce el segundo término: "))
var_c=int(input("Introduce el tercer término: "))

var_raiz=(var_b**2)-(4*var_a*var_c)

if var_raiz>0:
    var_x1=(((-var_b)+math.sqrt(var_raiz))/2*var_a)
    var_x2=(((-var_b)-math.sqrt(var_raiz))/2*var_a)
    print("El valor de x1 es: ",var_x1)
    print("El valor de x2 es: ",var_x2)

else:
    print("La raíz no puede ser un valor negativo")    