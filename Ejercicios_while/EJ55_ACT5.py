#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
suma=0
suma_tot=0
num_s_n=1

while suma_tot%2==0 or suma_tot<50:
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
print(f"Resumen: la suma total es {suma} y el número total de repeticiones es: {num_s_n}")