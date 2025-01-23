#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
tab_mult=0
contador=1

tab_mult=int(input("Introduce un número: "))

while contador<=10:
    print(f"{tab_mult*contador}")
    contador +=1
    
print("Fin del programa")