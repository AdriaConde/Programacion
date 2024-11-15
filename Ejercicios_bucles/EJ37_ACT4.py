#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
número=input("Introduce el número de notas que vas a introducir: ")
try:
    entero=int(número)
    for contador in range(entero):
        nota=float(input("Introduce la nota:"))
        if nota>5:
            print("Asignatura aprobada")
        else:
            print("Asignatura suspendida")
    
except ValueError:
    print("Error")