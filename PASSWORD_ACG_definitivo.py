#Mitjançant la instrucció \n que executa un salt de línea en un mateix print, he escrit les instruccions en tan sols 2 prints.
print("INSTRUCCIONS\n1. La longitud del password ha de tenir una longitud d'entre 6 i 8 caràcters\n2. Forçar els següents valors segons la posició indicada")
print("      Posició 1 Un número major o igual 1 i menor o igual a 5\n      Posició 2 Una lletra minúscula\n      Posició 3 Una lletra majúscula\n      Posició 4 Un dels següents sí­mbols *, _, @\n      Posició 5 Una lletra minúscula\n      Posició 6 Un número major o igual a 6 i menor o igual a 9\n      Posició 7 Un dels següents sí­mbols &, /, #\n      Posició 8 Un número menor o igual a 5")
#Pido mediante input que introduzcan PASSWORD por pantalla.
password=input("Introdueix una paraula clau: ")
#He inicialitzat la variable que contabilitza el nombre d'errors, més tard veurem el seu ús.
var_errores=0

#Faig aquesta primera condició per a que em salti error de longitud, sense comprovar si el valor d ela posició de l'índex és correcte.
if len(password)>=6 and len(password)<=8:
    
    #En les següents 5 condicions, segueixo el mateix codi: primer estableixo el valor inorrecte, si entra a la condició printejo "Error en el caràcter pertinent", seguit d'un "end=" "" que fa que un seguit de missatges es printejin en una mateixa línea. Finalment sumo 1 a la variable "var_errores", per a marcar que el PASSWORD introduït és inperfecte.
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
    
    #En aquesta verificació, he escrit el mateix codi que les anteriors condicions, però afeigeixo un codi per a comprovar si és correcte: primer comprovo si la longitud és correcta, després si entra la condició miro si la "var_errores" és igual a 0, per tant és perfecta. Si és així, printejo que el PASSWORD és correcte.
    if password[5]<str(6) or password[5]>str(9):
        print("Error en el caràcter 6", end=" ")
        var_errores=var_errores+1
    if len(password)==6:
        if var_errores==0:
            print("El format del PASSWORD és correcte")

    #Ídem a la verificació del caràcter 6, però utilitzo elifs en comptes d'ifs.
    elif password[6] not in ["&", "/", "#"]:
        print("Error en el caràcter 7", end=" ")
        var_errores=var_errores+1
    elif len(password)==7:
        if var_errores==0:
            print("El format del PASSWORD és correcte")
            
    #ídem al codi del caràcter 7, però com després d'una sèrie d'elifs s'utilitza un else.                    
    elif password[7]>str(5):
        print("Error en el caràcter 8")  
        var_errores=var_errores+1
    else:
        if var_errores==0:
            print("El format del PASSWORD és correcte")
 
else:
    print(f"Error, el password té una longitud de {len(password)} carècters i no compleix els requisits")