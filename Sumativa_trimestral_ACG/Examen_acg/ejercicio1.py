#Ejercicio1
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("******************")
var_tipo=input("Escoja el tipo de combustible: ")
var_litros=int(input("Introduzca el número de litros a repostar: "))

if var_tipo=="1":
    print("El total a pagar es: ", 1.765*var_litros)

if var_tipo=="2":
    var_total=1.913*var_litros
    var_descuento1=var_total-((var_total/100)*10)
    print(f"El total a pagar es {var_total} y con el descuento queda en {var_descuento1}")
    
if var_tipo=="3":
    print("El total a pagar es: ", 1.746*var_litros)
    
if var_tipo=="4":
    var_total2=1.839*var_litros
    var_descuento2=var_total2-((var_total2/100)*12)
    print(f"El total a pagar es {var_total2} y con el descuento queda en {var_descuento2}")