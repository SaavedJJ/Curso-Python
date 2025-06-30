###
# 01 - Sentencias condicionales if, elif, else
# Permiten ejecutar una secuencia de comandos dependiendo de una condición
###

import os 
os.system("cls")

edad = 18                                  # en el momento que una condición sea verdadera, 
if edad >= 18:                             # se ejecuta el bloque correspondiente y sale del if
    print("Eres mayor de edad")              
elif edad >= 16:
    print(f"Tienes {edad} años")
else:
    print("Eres menor de edad")
    


print("\n Condiciones multiples")

edad = 18
carnet = True

if edad >= 18 and carnet:
    print("puedes conducir")
else:
    print("POLICIA!! 🚔")
    
    
    
if edad >= 18 or carnet:
    print("puedes conducir en la isla margarita")
else:
    print("paga al policia y te deja conducir")
    
    
es_fin_de_semana = False
if not es_fin_de_semana:
    print("Toca currar")
    

print("\n Anidar condiciones")

edad = 18                                                        # La condiciones anidadas no son recomendadas
tiene_dinero = True                                              # pero son una forma de crear flujos de control
if edad >= 18:                                                   # que puede ser útil para crear condiciones complejas
    if tiene_dinero:
        print("Salir de discoteca")
    else:
        print("No tienes dinero")
else:
    print(f"No puedes ir a la discoteca con {edad} años")
    
