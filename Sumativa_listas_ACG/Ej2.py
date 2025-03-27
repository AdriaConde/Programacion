#EJ2
milista=[]
frase=""
frase2=""
cant=0

frase=input("Introduce la frase deseada: ")
milista=frase.split(" ")

print(f"Lista de palabras:")
print(milista)
      
cant=milista.count("de")
print(f"La palabra DE aparece {cant} veces")

milista.set()
print(milista)