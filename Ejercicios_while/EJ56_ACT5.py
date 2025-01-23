#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. El establecimiento contempla los siguientes descuentos:Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:• El número de pedidos realizados• Total a pagar.• Total con IVA (10%)• Total con el descuento aplicado.
s_n="s"
num_s_n=1
total=0
total_IVA=0
m=0
a=0
b=0
desc_5=0
desc_15=0

print("Menú \n1. Bocadillo de calamares - 9€ \n2. Bocadillo de chistorra - 4.5€ \n3. Bikini de jamón - 2.5€ \n")
print("Acompañamiento \n1. Patatas fritas - 1.5€ \n2. Patatas gruesas - 1.75€ \n3. Patatas rústicas - 2€ \n")
print("Bebidas \n1. Coca cola - 2€ \n2. Acuarius - 1.5€ \n3. Agua - 1€ \n")

while s_n=="s":
    m=int(input("Selecciona un bocadillo: "))
    if m==1:
        total +=9
    if m==2:
        total +=4.5
    if m==3:
        total +=2.5
    a=int(input("Selecciona un acompañamiento: "))
    if a==1:
        total +=1.5
    if a==2:
        total +=1.75
    if a==3:
        total +=2
    b=int(input("Selecciona una bebida: "))
    if b==1:
        total +=2
    if b==2:
        total +=1.5
    if b==3:
        total +=1
    s_n=input("Deseas hacer otro pedido? s/n: ")
    if s_n=="s":
        num_s_n+=1

total_IVA=(total*10/100)+total

if total<20:
    print(f"RESUMEN: \nNúmero de pedidos: {num_s_n} \nTotal a pagar: {total} \nTotal con IVA: {total_IVA} \nNo hay descuento.")
if total>20 and total<30:
    desc_5=total-(total*5/100)
    print(f"RESUMEN: \nNúmero de pedidos: {num_s_n} \nTotal a pagar: {total} \nTotal con IVA: {total_IVA} \nPrecio total con descuento del 5%: {desc_5}")
if total>30:
    desc_15=total-(total*15/100)
    print(f"RESUMEN: \nNúmero de pedidos: {num_s_n} \nTotal a pagar: {total} \nTotal con IVA: {total_IVA} \nPrecio total con descuento del 15%{desc_15}")