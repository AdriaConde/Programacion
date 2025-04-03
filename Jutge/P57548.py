milista=[]

var1=input()
milista=var1.split(" ")

if len(milista)==1:
    var2=int(input())
    milista.append(var2)

milista1=[int(x) for x in milista]

print(sum(milista1))