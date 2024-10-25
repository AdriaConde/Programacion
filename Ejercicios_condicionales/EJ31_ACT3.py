#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
txt="A quién madruga Dios le ayuda"
var1=input("Introduce una palabra:")

if var1 in txt:
    var2=txt.find(var1)
    print(f"La palabra está en la frase y está en el índice {var2}")
else:
    print("La palabra no está en la frase")