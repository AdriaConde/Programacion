#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
milista=[]
numero=0

var_cantidad=int(input("¿Cuántos números quieres? "))

for recorrer in range(0,var_cantidad):
    numero=int(input("Introduce un número: "))
    milista.append(numero)

milista.sort()
    
print(milista)