###
# 03 - casting de types
# transformar un tipo de un valor a otro
###

import os 
os.system("cls")

print("Conversion de tipos")
print(type(int("100")))

print(int("100") + 2)
print("100" + str(2))

print(int(3.1416))
print(int(2.9)) # no hace operaciones de redondeo
print(round(3.5)) # redondea al par mas cercano 

print(float(int(3.1416))) # destruye los decimales y al volver a convertir a float queda como '.0'

# print(int("hola mundo")) 

print(bool(1))
print(bool(2))
print(bool(0)) # el unico valor numerico que se convierte a False es el '0'
print(bool(-1))

print(bool("")) # la unica cadena str que se convierte a False es la vacia, por ausencia de contenido
print(bool(" ")) 
print(bool("False"))




