listanum=[]
listaletra=[]
valores=input("Introduce valores: ")
milista1=valores.split("-")

for recorrer in milista1:
    if recorrer.isnumeric():
        listanum.append(int(recorrer))
        
    else:
        if "." in recorrer:
            listanum.append(float(recorrer))
        else:
            listaletra.append(recorrer)
            
print(listanum)
print(sum(listanum))

listanum=set(listanum)
print(listanum)
print(sum(listanum))