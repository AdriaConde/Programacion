print("INSTRUCCIONS")
print("1. La longitud del password ha de tenir una longitud d'entre 6 i 8 carácters")
print("2. Forçar els següents valors segons la posició indicada")
print("      Posició 1 Un número major o igual 1 i menor o igual a 5")
print("      Posició 2 Una lletra minúscula")
print("      Posició 3 Una lletra majúscula")
print("      Posició 4 Un dels següents símbols *, _, @")
print("      Posició 5 Una lletra minúscula")
print("      Posició 6 Un número major o igual a 6 i menor o igual a 9")
print("      Posició 7 Un dels següents símbols &, /, #")
print("      Posició 8 Un número menor o igual a 5")
password=input("Introduce una palabra clave: ")

if len(password)<6 or len(password)>8:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
elif password[0]<1 or password[0]>5:
        print("Error en el carácter 1")
else:
    print("ok")