#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas: a) total de pares b) total de impares c) total de números positivos d) total de números negativos e) total de ceros f) total de la suma de todos los números introducidos
num=0
tot=0
num_neg=0
num_pos=0
num_par=0
num_impar=0
num_c=0

while num!=-99:
    num=int(input("Introduce un número: "))
    if num!=-99:
        tot=num+tot
        if num<0:
            num_neg +=1
        if num>=0:
            num_pos +=1
        if num%2==0:
            num_par +=1
        if not num%2==0:
            num_impar +=1
        if num==0:
            num_c +=1

print(f"RESUMEN \nEl número de pares es: {num_par} \nEl número de impares es {num_impar} \nEl número de positivos es: {num_pos} \nEl número de negativos es: {num_neg} \nEl número de ceros es: {num_c} \nEl total es: {tot}")