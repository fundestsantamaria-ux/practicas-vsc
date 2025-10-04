#-------------------------------
# Enunciado condicional - 1
#-------------------------------

# Los enunciados condicionales permiten ejecutar diferentes bloques de código
#   basados en si una condición es verdadera o falsa. El enunciado condicional
#       más común en Python es el "if".

# La estructura básica de un enunciado condicional es:
# if condición:
#     bloque de código si la condición es verdadera
# else:
#     bloque de código si la condición es falsa
# La condición es una expresión que se evalúa como True o False.
# El bloque de código dentro del if o else debe estar indentado (generalmente con 4 espacios).



numero = int(input("Ingresa un número: "))

# Condición para saber si es par o impar
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")


###################

# Se pide una nota
nota = float(input("Ingresa tu nota: "))

# Se evalúa si la nota es mayor o igual a 70 (aprobado)
if nota >= 71:
    print("Aprobaste")
else:
    print("Reprobaste")

# En Panamá, la nota mínima aprobatoria es 71.
# En Republica Dominicana, la nota mínima aprobatoria puede ser 70.
