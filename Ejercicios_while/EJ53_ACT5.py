#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While.
s_n="s"
suma=0
num_s_n=1

while s_n=="s":
    n_1=int(input("Introduce un primer valor: "))
    n_2=int(input("Introduce un segundo valor: "))
    suma=n_1+n_2
    print(f"El resultado de la suma es {suma}")
    suma=suma+suma
    s_n=input("Deseas repetir la operación? s/n: ")
    if s_n=="s":
        num_s_n+=1

print(f"Resumen: la suma total es {suma} y el número total de repeticiones es {num_s_n}")