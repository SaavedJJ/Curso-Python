###
# 04 - variables
# lenguaje de tipado dinamico y fuerte
###

import os 
os.system("cls")

my_name = "socrates"
print(my_name)

age = 22
print(age)

age = 23
print(age)

# IMPORTANTE!! TIPADO DINAMICO Puede alterarse el tipo de varible en tiempo de ejecucion
string = "hola"
print(type(string))

string  = 1234
print(type(string))

# IMPORTANTE!! TIPADO FUERTE No se realizan conversiones automaticas
# print(10 + "2")

print(f"Hola soy {my_name} y tengo {age} años")

# RECOMENDACION Como no asignar variables
name, age, city = "socrates", 22, "Montevideo"

# Convencion de nombres de variable
mi_variable_es_esta = "ok" # snake_case, recomendado
mi_variable_es_esta_123 = "ok"

MiVariableEsEsta = "ko" # No recomendado, CamelCase
mivariableesesta = "ko" # No recomendado, todojunto

# nombres de variables no validos
# 1234_mi_variable = "ko" # No puede empezar con numero
# mi-variable = "ko" # No puede tener guion
# mi variable = "ko" # No puede tener espacios
# palabras reservadas = "ko" # No puede ser una palabra reservada de python

# las palabras reservadas son:S
# False, None, True, and, as, assert, async, await, break, class, continue,
# def, del, elif, else, except, finally, for, from, global, if, import,
# in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

MI_CONSTANTE = 3.14 # No exiten constantes en python, pero se recomienda usar mayusculas para indicar que no deben cambiar

# Tipado
is_user_logged_in: bool = True # booleano
print(is_user_logged_in)

# is_user_logged_in = 41
print(is_user_logged_in) # No se recomienda cambiar el tipo de variable, pero es posible
