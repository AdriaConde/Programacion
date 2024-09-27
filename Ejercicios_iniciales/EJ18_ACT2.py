#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
var_ninos=int(input("¿Cuantos menores?"))
var_adultos=int(input("¿Cuantos adultos?"))
var_precio=12
var_pn=var_precio-((50*12)/100)
var_pa=var_precio-((10*12)/100)
print(f"El precio total del cine para {var_ninos} menor/es es:", round(var_pn*var_ninos,1))
print(f"El precio total del cine para {var_adultos} adulto/s es:", round(var_pa*var_adultos,1))
