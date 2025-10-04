#---------------------------------
# Que es la Planificacion de la programacion?
#---------------------------------
# La planificación de la programación es el proceso de organizar y estructurar las tareas y actividades necesarias para desarrollar 
#   un programa de software. Implica definir los objetivos, identificar los recursos necesarios, establecer un cronograma y asignar 
#       responsabilidades a los miembros del equipo de desarrollo.

# Una buena planificación ayuda a asegurar que el proyecto se complete a tiempo, dentro del presupuesto y cumpliendo 
#   con los requisitos establecidos.

# La planificación de la programación puede incluir varias etapas, como:
# 1. Definición de requisitos: Identificar las necesidades y expectativas del cliente o usuario final.
# 2. Análisis de viabilidad: Evaluar si el proyecto es factible en términos de recursos, tiempo y tecnología.
# 3. Diseño del sistema: Crear una arquitectura y un diseño detallado del software.

#-------------------------------------------------
# Programa para calcular el área de un rectángulo
#-------------------------------------------------

# Se pide la base y la altura al usuario

# ENTEROS Y DECIMALES
# INT = ENTEROS 10, -5, 30
# FLOAT = DECIMALES 10.5, -3.2, 0.75

#INPUT = ENTRADA DE DATOS

base = float(input("Ingresa la base en decimal: "))
altura = float(input("Ingresa la altura en decimal: "))

# Se calcula el área multiplicando base * altura
area = base * altura

# Se muestra el resultado en pantalla
print("El área del rectángulo es:", area)


#############

# Conversor de Celsius a Fahrenheit

# Se pide una temperatura en grados Celsius
celsius = float(input("Temperatura en °C: "))

# Fórmula de conversión: (°C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Se imprime la temperatura en Fahrenheit
print("Temperatura en °F:", fahrenheit)











#---------------------------------
# Logica secuencial de un robot
#---------------------------------
#Mi robor va realizar 10 pasos con movimientos secuenciales de pie izquierda, derecha, adelante y atras
print("Mi robot va a realizar 10 pasos")

# Brazo izquierdo, levanta un host
print("Brazo izquierdo, levanta un host")

# El robot da una media vuelta y avanza
print("El robot da una media vuelta y avanza")

# El robot realiza 10 pasos y se detiene cuando llega a la meta
print("El robot realiza 10 pasos y se detiene cuando llega a la meta")
