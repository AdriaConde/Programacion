#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While.
num_bd=int(input("Cuántos buenos días? "))
contador=0

while contador<num_bd:
    print("Buenos días")
    contador +=1