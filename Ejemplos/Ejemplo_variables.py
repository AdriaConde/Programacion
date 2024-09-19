#definicion de 3 tipos de variables

var_entero=4
var_dec=3.5
var_texto="hola"

print(var_entero)
print(var_dec)
print(var_texto)


#maneras de visualizar informacion

#manera 1 añadir texto entre comillas, separando con comas las variables
print("el resultado es:",var_entero, "manzanas")

var_total=var_entero+var_dec

print("el resultado es:", var_total)

#manera 2, con formato (f)
print(f"el resultado de sumar {var_entero} + {var_dec} es:", var_total)
