###
# 05 - input()
# La funcion input() permite al usuario introducir datos desde el teclado.
###

name = input("Introduce tu nombre: \n")
print(f"Hola, {name}!")

age = input("Cuantos años tienes?: \n")
print(type(age))
print(f"Tienes {int(age) + 1} años.")

print("Obtener multiples valores")
name, age = input("Introduce tu nombre y edad separados por un espacio: \n").split()
print(f"Hola, {name}! El año que viene tendras {int(age) + 1} años.")
