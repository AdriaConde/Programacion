passw=input("Introduce una contraseña: ")

while len(passw)!=8:
    print("very bad")
    passw=input("try again: ")

else:
    print("very good")