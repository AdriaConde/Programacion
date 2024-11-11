print("INSTRUCCIONS")
print("1. La longitud del password ha de tenir una longitud d'entre 6 i 8 caràcters")
print("2. Forçar els següents valors segons la posició indicada")
print("      Posició 1 Un número major o igual 1 i menor o igual a 5")
print("      Posició 2 Una lletra minúscula")
print("      Posició 3 Una lletra majúscula")
print("      Posició 4 Un dels següents sí­mbols *, _, @")
print("      Posició 5 Una lletra minúscula")
print("      Posició 6 Un número major o igual a 6 i menor o igual a 9")
print("      Posició 7 Un dels següents sí­mbols &, /, #")
print("      Posició 8 Un número menor o igual a 5")
password=input("Introduce una palabra clave: ")
var_errores=0

if len(password)>=6 and len(password)<=8:
    if password[0]<str(1) or password[0]>str(5):
        print("Error en el caràcter 1")
        var_errores=var_errores+1
    if password[1].islower()==False:
        print("Error en el caràcter 2")
        var_errores=var_errores+1
    if password[2].islower()==True:
        print("Error en el caràcter 3")
        var_errores=var_errores+1
    if not password[3]=="*" and password[3]=="_" and password[3]=="@":
        print("Error en el caràcter 4")
        var_errores=var_errores+1
    if password[4].islower()==False:
        print("Error en el caràcter 5")
        var_errores=var_errores+1
    if len(password)==6:
        if not password[5]<str(6) or password[5]>str(9) and var_errores==0:
            print("El format del PASSWORD és correcte")
        if password[5]<str(6) or password[5]>str(9):
            print("Error en el caràcter 6")
    if len(password)==7:
        if password[6]=="&" and password[6]=="/" and password[6]=="#" and var_errores==0:
            print("El format del PASSWORD és correcte")
        if not password[6]=="&" and password[6]=="/" and password[6]=="#":
            print("Error en el caràcter 7")
    if len(password)==8:
        if not password[7]>str(5) and var_errores==0:
            print("El format del PASSWORD és correcte")
        if password[7]>str(5):
            print("Error en el caràcter 8")
 
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")