#Objetivos de la clase

#Instalar y usar la librería pandas.
#Diferenciar entre Serie y DataFrame.
#Crear series a partir de listas y diccionarios.
#Seleccionar elementos y hacer operaciones con series.
#Representar datos en gráficos básicos.


#Instalar y usar la librería pandas

# Si no tienes pandas instalado, descomenta la siguiente línea:
# pip install pandas   
#import pandas as pd  # Importamos pandas con el alias pd

#Diferenciar entre Serie y DataFrame


#Serie (Series): es como una columna (datos en una sola dimensión, con índice).
#DataFrame: es como una tabla completa (varias columnas y filas).

# Ejemplo en series

#import pandas as pd  # Importamos la librería pandas

#Ejemplo 1: Serie (una sola columna)
#numeros = pd.Series([10, 20, 30, 40])
#print("Ejemplo de Serie:")
#print(numeros)

#Explicación:
# A la izquierda está el índice (0,1,2,3) y a la derecha los valores.
# Es como una sola columna de datos.


#Salida de la Serie:

#0    10
#1    20
#2    30
#3    40

#dtype: int64

#
#=====================================================

# Ejemplo 2: DataFrame (tabla con filas y columnas)

#import pandas as pd  # Importamos la librería pandas

#personas = pd.DataFrame({
    #"Nombre": ["Jefry Castilo", "Randy Serra", "Alexa Rodriguez"],
    #"Edad": [40, 32, 25]
#})
#print("\nEjemplo de DataFrame:")
#print(personas)

# Explicación:
# Ahora tenemos una tabla con dos columnas: "Nombre" y "Edad".
# Cada fila tiene un índice (0,1,2) que identifica a cada persona.

#Salida del DataFrame:


#Nombre  Edad
#0    Ana    25
#1   Luis    30
#2  Pedro    22


#En resumen:

#Una Serie = columna individual (1D).
#Un DataFrame = tabla con varias columnas (2D).


# Grafico sencillo con matplotlib.pyplot
# Matplotlib es otra librería popular para gráficos
# Si no la tienes instalada, descomenta la siguiente línea: 
# pip install matplotlib


#import matplotlib.pyplot as plt

#edades = pd.Series([15, 25, 35, 45, 55], index=["Ana", "Luis", "Marta", "José", "Laura"])
#edades.plot(kind="bar")  # gráfico de barras
#plt.show()
