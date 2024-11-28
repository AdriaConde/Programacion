#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.
palabra_secreta=input("Introduce la palabra secreta: ")

for contador in range(len(palabra_secreta)):
    letra=input("Introduce la letra: ")
    if letra in palabra_secreta:
        print("La letra existe")
    else:
        print("La letra no existe")