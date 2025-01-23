#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
s_n="s"

while s_n=="s":
    n_1=int(input("Introduce un primer valor: "))
    n_2=int(input("Introduce un segundo valor: "))
    print(f"El resultado de la suma es {n_1+n_2}")
    s_n=input("Deseas repetir la operación? s/n: ")

print("Programa finalizado")