#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra. 
var=input("Introduce una palabra: ")

for contador in range(len(var)):
    letra=input("Introduce la letra: ")
    if letra not in var:
        print("Error")
   
    for contador in range(len(var)):
        if letra==var[contador]:
            print(f"La letra {letra} se encuentra en la posición", contador+1)