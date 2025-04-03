milista=[]

var1=input()
milista=var1.split(" ")

if len(milista)!=5:
    var2=input()
    if len(var2)==0:
        var2=int(input())
        milista.append(var2)

milista1=[int(x) for x in milista]

print(sum(milista1))