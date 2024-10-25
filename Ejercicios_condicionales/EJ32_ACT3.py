#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
txt="A quién madruga Dios le ayuda"
var1=input("Introduce una palabra:")

txt_2=txt.lower()
var1_2=var1.lower()

if var1_2 in txt_2:
    var2=txt_2.find(var1_2)
    print(f"La palabra está en la frase y está en el índice {var2}")
else:
    print("La palabra no está en la frase")