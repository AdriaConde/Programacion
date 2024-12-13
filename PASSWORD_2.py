#Password2
print("INSTRUCCIONS\n1. La longitud del password ha de tenir una longitud de 8 caràcters\n2. Hauràn 2 lletres minúscules i una mayúscula\n3. Hauràn 3 nombres, que han de ser majors o iguals a 5 i menor o igual a 8\n4. Hauràn 2 símbols, que han de ser: %, / o *")

for contador in range (0, 3):
    var_letra=0
    var_letra_may=0
    var_num=0
    var_simb=0
    PASSWORD=input("Introdueix una paraula clau: ")
    
    if len(PASSWORD)==8:
        for letra in PASSWORD:
            if letra.islower()==True:
                var_letra=var_letra+1
            if letra.isupper()==True:
                var_letra_may=var_letra_may+1
            if letra.isnumeric()==True and letra in ["5", "6", "7", "8"]:
                var_num=var_num+1
            if letra in ["%", "/", "*"]:
                var_simb=var_simb+1
            if var_letra==2 and var_letra_may==1 and var_num==3 and var_simb==2:
                print("El format del PASSWORD és correcte")
            var_total=var_letra+var_letra_may+var_num+var_simb
            if not (var_letra==2 and var_letra_may==1 and var_num==3 and var_simb==2) and var_total==8:
                if not var_letra==2:
                    print("Error a les lletres minúscules")
                if not var_letra_may==1:
                    print("Error a les lletres majúscules")
                if not var_num==3:
                    print("Error als nombres")
                if not var_simb==2:
                    print("Error als símbols")
    else:
        print("El format del PASSWORD no és correcte")