#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
milista=[]
milista_2=[]
numero=0
var_cantidad=0

var_cantidad=int(input("Introduce cantidad de palabras: "))

for recorrer in range(0,var_cantidad):
    numero=(input("Introduce una palabra: "))
    milista.append(numero)

milista.sort()
print(milista)

milista_2=milista.copy()
milista_2.reverse()
print(milista_2)