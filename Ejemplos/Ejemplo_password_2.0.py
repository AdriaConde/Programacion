#3 n√∫meros
#3 letras
#2 s√≠mbolos

#Contadores que cuentan el tipo de valor
contNum1_5=0
contNum6_9=0
contLetMay=0
contLetMin=0
contSimb=0

#variables m√°ximo
maxNum1_5=2
maxNum6_9=1
maxLetMay=2
maxLetMin=1
maxSimb=2

#esta variable me informa si el password cumple los 8 criterios
chivato=0

for contador in range (0,3):
    password=input("Introduce un password")
    
    for recorrer in password:
        if recorrer.isnumeric()==True:
            if recorrer in "12345":
                contNum1_5=contNum1_5+1
            if recorrer in "6789":
                contNum6_9=contNum6_9+1
        if recorrer.isupper()==True:
            contLetMay=contLetMay+1
        if recorrer.islower()==True:
            contLetMin=contLetMin+1
        if recorrer in "&%#*/":
            contSimb=contSimb+1
    
    if contNum1_5<maxNum1_5:
        print(f"Error, falta por introducir {maxNum1_5-contNum1_5} n˙meros del 1 al 5")
    else:
        chivato=chivato+1
        
    if contNum6_9<maxNum6_9:
        print(f"Error, falta por introducir {maxNum6_9-contNum6_9} n˙meros del 6 al 9")
    else:
        chivato=chivato+1
        
    if contLetMay<maxLetMay:
        print(f"Error, falta por introducir {maxLetMay-contLetMay} letras may˙sculas")
    else:
        chivato=chivato+1
        
    if contLetMin<maxLetMin:
        print(f"Error, falta por introducir {maxLetMin-contLenMin} letras min˙sculas")
    else:
        chivato=chivato+1
            
    if contSimb<maxSimb:
        print(f"Error, falta por introducir {maxSimb-contSimb} s√≠mbolos")
    else:
        chivato=chivato+1