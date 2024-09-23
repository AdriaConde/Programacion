#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var_base_menor=float(input("La base menor es:"))
var_base_mayor=float(input("La base mayor es:"))
var_altura=float(input("La altura es:"))
var_lado=float(input("El es:"))
var_perimetro=var_base_menor+var_base_mayor+(2*var_lado)
print("El perímetro es:", var_perimetro)
var_area=((var_base_menor+var_base_mayor)*var_altura)/2
print("El área es:",var_area)
