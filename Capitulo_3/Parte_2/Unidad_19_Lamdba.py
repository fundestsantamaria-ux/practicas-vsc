# Una lambda es una función pequeña que se 
# escribe en una sola línea.
# Se usa para cosas rápidas, sin tener que escribir def.
# Sintaxis:

#lambda argumentos: operación

#Funciones Lambda (Funciones Anónimas)


#======================

from functools import reduce  # Necesario para usar reduce

# Tenemos una lista de números
numeros = [1, 2, 3, 4, 5, 6]

# FILTER -> quedarnos con los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)  # [2, 4, 6]

# MAP -> multiplicar cada número por 10
multiplicados = list(map(lambda x: x * 10, numeros))
print("Multiplicados:", multiplicados)  # [10, 20, 30, 40, 50, 60]

# REDUCE -> sumar todos los números
suma = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma)  # 21

#======================


# Con def
#def cuadrado(x):
    #return x * x
    #print("Hola")  # Esta línea nunca se ejecuta


#def cuadrado(a, b): 
    #return a * b

# Con lambda
#cuadrado_lambda = lambda x: x * x

#print(cuadrado(5))        # 25
#print(cuadrado_lambda(5)) # 25




#============================ RD15

lista_rd15 = [('Johan',8.0),
              ('Jose',7.1),
              ('Wandrys',9.0),
              ('Jeremy',6.5),
              ('Randolf',4.5),
              ('Eimy',8.5)]

#lista_ordenada = sorted(lista_estudiantes,key= lambda x:x[1], reverse=True)

#print(lista_ordenada)  # Ordena por la segunda posición (nota)


#============================ RD16


lista_rd16 =[('Angel Bather',6.0),
            ('Josias Paguero',6.5),
            ('Alexa Rodriguez',9.5),
            ('Erick Caraballo',7.5),
            ('Jenry Sanchez',8.5),
            ('Melvin Garcia',9.0),
            ('Randy Serra',4.0)]



lista_excelencia = sorted(lista_rd16,key= lambda x:x[1], reverse=True)
print(lista_excelencia)  # Ordena por la segunda posición (nota)


#lista_excelencia = sorted(lista_rd16, key= lambda x:x[1], reverse=False)
#print(lista_excelencia)  # Ordena por la segunda posición (nota)
