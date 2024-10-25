precio1=5
precio2=4

print("1. Gladiator")
print("2. Titanic")
print("3. Interestelar")

var_menu=input("Introduce una opción: ")

if var_menu.isnumeric()==True:
    if var_menu=="1" or var_menu=="3":
        print(f"El precio es {precio1} €")
    elif var_menu=="2":
        print(f"El precio es {precio2} €")
    else:
        print("error")
    
else:
    print("No es un número")

#if var_menu>1 or var_menu<4:
    #print("error")

print("programa finalizado")