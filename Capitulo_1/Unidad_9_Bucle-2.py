#-------------------------------------------------
# Unidad 9: Bucle-2
#-------------------------------------------------
# Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.
#   Esto es útil para tareas que requieren repetición, como procesar elementos en una lista
#       o realizar cálculos iterativos.

#Comparación entre repetir código y usar bucles: Utilizando bucle FOR
# Sin bucles:
print("Hola, Alejandra")
print("Hola, Ana")
print("Hola, Alejandro")
print("Hola, Alexander")
# Con bucles:
for nombre in ["Alejandra", "Ana", "Alejandro", "Alexander"]:
    print("Hola", nombre)


# Python soporta varios tipos de bucles, siendo los más comunes "for" y "while".

# La estructura básica de un bucle "while" es:
# while condición:
#     bloque de código a ejecutar mientras la condición sea verdadera
# La condición es una expresión que se evalúa como True o False.
# El bloque de código dentro del bucle debe estar indentado (generalmente con 4 espacios).


#Características:
#Repite el bloque mientras la condición sea True.
#Necesitas manejar manualmente una variable de control (ej: contador).
#Si olvidas actualizar esa variable → se crea un bucle infinito.

# Lista de nombres
nombres = ["Ana", "Carlos", "Laura", "Pedro"]

i = 0  # inicializamos el contador ,  Variable de control
while i < len(nombres):  # condición
    print("Hola", nombres[i])
    i += 1  # incrementamos el contador



#################

# Repetir hasta que la variable sea mayor o igual a 5
contador = float(input("Ingresa un número: ")) # X puede variar

while contador < 110:
    print("Contador en:", contador)
    contador += 10  # Incrementa en 1 cada vez





