#Objetivos de la clase

#Comprender qué son los módulos y por qué se agrupan en funciones, clases, variables y códigos reutilizables.
#Aprender a usar import, from, y as según la necesidad.
#Generar números aleatorios con el módulo random.
#Trabajar con fechas y horas usando el módulo datetime.

#Conceptos:

#Un módulo es un archivo .py que contiene funciones, clases o variables listas para usarse.
#Nos permiten reutilizar código en lugar de escribirlo todo desde cero.
#Python tiene muchos módulos integrados (ej: math, random, datetime).
#También se pueden crear módulos propios o instalar externos.

# Ejemplo 1: Importar y usar funciones de un módulo
# Importamos el módulo math para usar funciones matemáticas

#import math

# Usamos algunas funciones del módulo
#print("Raíz cuadrada de X:", math.sqrt(400))   # sqrt = raíz cuadrada
#print("Número pi:", math.pi)                   # constante pi


#Ejemplo 2: Usar from y as

# Importamos solo la función sqrt desde math
#from math import sqrt

#print("Raíz cuadrada de 25:", sqrt(25))   # No necesitamos math.sqrt, solo sqrt

#=============================================
# Importamos math pero le damos un alias más corto

#import math as m
#print("Coseno de 0:", m.cos(0))


#Explicación:
#from math import sqrt trae solo esa función.
#import math as m crea un alias (muy útil para escribir menos).

#=============================================

#Ejemplo 3: Generar números aleatorios

#import random

# Número aleatorio entero entre 1 y 5
#print("Número aleatorio entero:", random.randint(1, 5))

# Número aleatorio decimal entre 0 y 1
#print("Número aleatorio decimal:", random.random())


#Explicación:
#randint(a,b) → número entero entre a y b.
#random() → número decimal entre 0 y 1.


#=============================================

#Ejemplo 4: Trabajar con fechas y horas

#import datetime  # Importamos la librería para trabajar con fechas y horas

# Obtener la fecha y hora actual
#ahora = datetime.datetime.now()
#print("Fecha y hora actual:", ahora)  

# Crear una fecha específica (ejemplo: Navidad 2025)
#cumple = datetime.date(2025, 12, 25)
#print("Navidad del 2025:", cumple)

# Sumar días a la fecha actual (ejemplo: mañana)
#mañana = ahora + datetime.timedelta(days=1)
#print("Mañana será:", mañana)



# Explicación sencilla:

#datetime.datetime.now() → obtiene la fecha y hora en este momento.
#Ejemplo: 2025-09-19 18:45:30

#datetime.date(2025, 12, 25) → crea una fecha exacta (25 de diciembre de 2025).

#datetime.timedelta(days=1) → sirve para sumar o restar tiempo.
#Aquí sumamos 1 día para calcular “mañana”.

#Así, el programa muestra:
#La fecha y hora actual 
#Navidad del 2025 
#Y qué día será mañana 