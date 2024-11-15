#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
número=input("Introduce el número de notas que vas a introducir: ")
try:
    entero=int(número)
    for contador in range(entero):
        nota=float(input("Introduce la nota: "))
        if nota>10 or nota<0:
            print("Has introducido una nota equivocada")
        else:
            if nota>5:
                print("Asignatura aprobada")
            else:
                print("Asignatura supendida")
    
except ValueError:
    print("Error")
