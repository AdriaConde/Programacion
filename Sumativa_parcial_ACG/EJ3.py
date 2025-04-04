#Ej.3
#He importado la librería math porque la necesitaremos para la raiz cuadrada (es un operador que no está en el sistema predeterminado)
import math
#El mismo código que en los ejercicios anteriores para pedir algo por pantalla, en este caso el valor de un lado. Int, porque el valor de entrada no lleva decimales, ni .0
var_a=int(input("Introduce el valor de un lado:"))
#He aplicado la fórmula dada, para la raíz cuadrada he usado math.sqrt(). He usado bastantes paréntesis para asegurarme que la jerarquia de operaciones es correcta
var_area=(math.sqrt(3)/4)*(var_a**2)
#Printeo sin texto, solo redondeo a dos decimales (,2)
print(round(var_area,2))
