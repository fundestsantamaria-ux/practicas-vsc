#---------------------------------
# Fundamentos de los tipos de datos numéricos y operaciones aritméticas
#---------------------------------

# Los tipos de datos numéricos son fundamentales en la programación, ya que permiten 
#   realizar cálculos y operaciones matemáticas.

# En Python, los tipos de datos numéricos más comunes son:
# 1. int: Representa números enteros, tanto positivos como negativos, sin decimales. Ejemplo: 5, -3, 0.
# 2. float: Representa números de punto flotante (decimales). Ejemplo: 3.14, -0.001, 2.0.
# 3. complex: Representa números complejos, que tienen una parte real y una parte imaginaria. Ejemplo: 2 + 3j, -1 - 4j.
# Ejemplo de número complejo = Complex
base = 10 
altura = 5.5

df = base * altura # Ejemplo de operacion imaginaria 
Fd = df + 2.5 # Ejemplo de operacion real y imaginaria


# Python soporta varias operaciones aritméticas básicas, como:
# - Suma (+)
# - Resta (-)
# - Multiplicación (*)
# - División (/) 
# - División entera (//) 
# - Módulo (%) 
# - Exponenciación (**) 



# Declaración de variables enteras y decimales
x = 10 # Entero
y = 3.10 # Decimal

# Operaciones aritméticas
print("Suma:", x + y)       # Suma de 10 + 3.10
print("División:", x / y)   # División de 10 / 3.10

#################

# Se pide un número decimal al usuario
numero = float(input("Ingresa un número: "))
# Se calcula el cuadrado del número
print("Cuadrado:", numero ** 2)

# Se calcula la raíz cuadrada
print("Raíz cuadrada:", numero ** 0.5)
