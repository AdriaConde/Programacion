#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulados. Para aquellos de vosotros que os fijeis en los detalles, controlar que el mensaje del acumulado es singular o plural. Con while
suma=0
suma_tot=0
num_s_n=1

while suma_tot<50:
    n_1=int(input("Introduce un primer valor: "))
    n_2=int(input("Introduce un segundo valor: "))
    suma=n_1+n_2
    if num_s_n==1:
        print(f"El resultado de la suma es {suma} y llevas {num_s_n} operación realizada")
    else:
        print(f"El resultado de la suma es {suma} y llevas {num_s_n} operaciones realizadas") 
    suma_tot=suma_tot+suma
    print(f"El total acumulado es {suma_tot}")

print("Fin del programa")
print(f"Resumen: la suma total es {suma} y el número total de repeticiones es {num_s_n}")