print("INSTRUCCIONS\n1. La longitud del password ha de tenir una longitud d'entre 6 i 8 caràcters\n2. Forçar els següents valors segons la posició indicada")
print("      Posició 1 Un número major o igual 1 i menor o igual a 5\n      Posició 2 Una lletra minúscula\n      Posició 3 Una lletra majúscula\n      Posició 4 Un dels següents sí­mbols *, _, @\n      Posició 5 Una lletra minúscula\n      Posició 6 Un número major o igual a 6 i menor o igual a 9\n      Posició 7 Un dels següents sí­mbols &, /, #\n      Posició 8 Un número menor o igual a 5")
password=input("Introdueix una paraula clau: ")
var_errores=0

if len(password)>=6 and len(password)<=8:
    
    if password[0]<str(1) or password[0]>str(5):
        print("Error en el caràcter 1", end=" ")
        var_errores=var_errores+1
        
    if password[1].islower()==False:
        print("Error en el caràcter 2", end=" ")
        var_errores=var_errores+1
        
    if password[2].islower()==True:
        print("Error en el caràcter 3", end=" ")
        var_errores=var_errores+1
        
    if password[3] not in ["*", "_", "@"]:
        print("Error en el caràcter 4", end=" ")
        var_errores=var_errores+1
        
    if password[4].islower()==False:
        print("Error en el caràcter 5", end=" ")
        var_errores=var_errores+1
     
    if password[5]<str(6) or password[5]>str(9):
        print("Error en el caràcter 6", end=" ")
        var_errores=var_errores+1
    if len(password)==6:
        if var_errores==0:
            print("El format del PASSWORD és correcte")
    
    elif password[6] not in ["&", "/", "#"]:
        print("Error en el caràcter 7", end=" ")
        var_errores=var_errores+1
    elif len(password)==7:
        if var_errores==0:
            print("El format del PASSWORD és correcte")
                        
    elif password[7]>str(5):
        print("Error en el caràcter 8")  
        var_errores=var_errores+1
    else:
        if var_errores==0:
            print("El format del PASSWORD és correcte")
 
else:
    print(f"Error, el password té una longitud de {len(password)} carècters i no compleix els requisits")