#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar essuperior o igual a 40.
tab_mult=0
contador=1
resultado=0

tab_mult=int(input("Introduce un número: "))

while contador<=10:
    resultado=tab_mult*contador
    print(f"{tab_mult*contador}")
    contador +=1
    if resultado>=40:
        contador=11
   
print("Fin del programa")