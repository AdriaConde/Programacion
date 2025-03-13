#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas
milista=[]
repetir="s"

while repetir=="s":
    letra=input("Introduce una letra: ")
    milista.append(letra)
    repetir=input("¿Deseas repetir? (s/n): ")
    
milista=set(milista)
print(milista)