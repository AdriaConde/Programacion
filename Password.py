print("INSTRUCCIONS")
print("1. La longitud del password ha de tenir una longitud d'entre 6 i 8 car�cters")
print("2. For�ar els seg�ents valors segons la posici� indicada")
print("      Posici� 1 Un n�mero major o igual 1 i menor o igual a 5")
print("      Posici� 2 Una lletra min�scula")
print("      Posici� 3 Una lletra maj�scula")
print("      Posici� 4 Un dels seg�ents s�mbols *, _, @")
print("      Posici� 5 Una lletra min�scula")
print("      Posici� 6 Un n�mero major o igual a 6 i menor o igual a 9")
print("      Posici� 7 Un dels seg�ents s�mbols &, /, #")
print("      Posici� 8 Un n�mero menor o igual a 5")
password=input("Introduce una palabra clave: ")
var_errores=0

if len(password)>=6 and len(password)<=8:
    if password[0]<str(1) or password[0]>str(5):
        print("Error en el car�cter 1")
        var_errores=var_errores+1
    if password[1].islower()==False:
        print("Error en el car�cter 2")
        var_errores=var_errores+1
    if password[2].islower()==True:
        print("Error en el car�cter 3")
        var_errores=var_errores+1
    if not password[3]=="*" and password[3]=="_" and password[3]=="@":
        print("Error en el car�cter 4")
        var_errores=var_errores+1
    if password[4].islower()==False:
        print("Error en el car�cter 5")
        var_errores=var_errores+1
    if len(password)==6:
        if not password[5]<str(6) or password[5]>str(9) and var_errores==0:
            print("El format del PASSWORD �s correcte")
        if password[5]<str(6) or password[5]>str(9):
            print("Error en el car�cter 6")
    if len(password)==7:
        if password[6]=="&" and password[6]=="/" and password[6]=="#" and var_errores==0:
            print("El format del PASSWORD �s correcte")
        if not password[6]=="&" and password[6]=="/" and password[6]=="#":
            print("Error en el car�cter 7")
    if len(password)==8:
        if not password[7]>str(5) and var_errores==0:
            print("El format del PASSWORD �s correcte")
        if password[7]>str(5):
            print("Error en el car�cter 8")
 
else:
    print(f"Error, el password t� una longitud de {len(password)} car�cters i no compleix els requisits")