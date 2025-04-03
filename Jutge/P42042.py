letra=input("")

if letra.isupper()==True:
    print("majuscula")
    
if letra.isupper()==False:
    print("minuscula")

if letra in ["A","E","I","O","U","a","e","i","o","u"]:
    print("vocal")

if not letra in ["A","E","I","O","U","a","e","i","o","u"]:
    print("consonant")