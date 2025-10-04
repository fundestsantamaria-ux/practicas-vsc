#-------------------------------------------------
# Bucle-1
#-------------------------------------------------
# Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
#   Esto es útil para tareas que requieren repetición, como procesar elementos en una lista
#       o realizar cálculos iterativos.

# Python soporta varios tipos de bucles, siendo los más comunes "for" y "while".

# La estructura básica de un bucle "for" es:
# for variable in secuencia:
#     bloque de código a ejecutar en cada iteración

df = ("Hola Mundo")
for df in range(3):
    print("Hola Mundo")         # in = en,  range = rango

#Características:
#Recorre directamente una secuencia (lista, tupla, rango, string, etc.).
#Python se encarga de avanzar por los elementos.
#No necesitas un contador manual.

# Bucle for con rango de números
# Recorre del 0 al 4
for i in range(5):
    print("Iteración número:", i)

#################


# Lista de nombres
nombres = ["Ana", "Carlos", "Laura", "Pedro"]

# Recorremos la lista con un for
for nombre in nombres:                  #  for i in nombre 
    print("Hola", nombre)               # print("Hola", i)

# Ejenplo sin bucle (repetitivo)
print("--Ana---")
print("--Carlos---")
print("--Laura---")
print("--Pedro---")


# Poner en practica lo aprendido
# Por que? Porque es mas eficiente y menos propenso a errores

#-------------------------------------------------