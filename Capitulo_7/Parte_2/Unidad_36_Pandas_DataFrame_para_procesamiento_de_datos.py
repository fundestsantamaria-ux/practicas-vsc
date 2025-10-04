#Unidad 36: Pandas DataFrame para el procesamiento de datos

#¿Qué es un DataFrame?

#Un DataFrame es una estructura de datos en Pandas que se parece a una tabla de Excel:
#Tiene filas y columnas.
#Cada columna puede tener un tipo de dato diferente (números, texto, fechas).
#Es bidimensional (como una matriz con nombres).



# 1.Crear un DataFrame desde un diccionario

import pandas as pd

# Crear un diccionario (estructura clave: valor)
datos = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 34, 29],
    "Ciudad": ["Madrid", "Panamá", "Lima"]
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(datos)

print(df)

# Salida:

#   Nombre  Edad  Ciudad
#0     Ana    23  Madrid
#1    Luis    34  Panamá
#2  Carlos    29    Lima



# 2.Renombrar filas, columnas e índices

# Renombrar columnas
df.rename(columns={"Nombre": "Nombres", "Edad": "Años"}, inplace=True)

# Renombrar índices
df.rename(index={0: "Fila1", 1: "Fila2", 2: "Fila3"}, inplace=True)

print(df)



#Crear un DataFrame desde un archivo externo
#Importar CSV
#df_csv = pd.read_csv("archivo.csv")  # Lee un archivo CSV

#Importar Excel
#df_excel = pd.read_excel("archivo.xlsx")  # Requiere instalar openpyxl

#Importar JSON
#df_json = pd.read_json("archivo.json")



#Obtener datos desde una API (ejemplo con Yahoo Finance)

import pandas_datareader.data as web
import datetime

# Fechas de inicio y fin
inicio = datetime.datetime(2020, 1, 1)
fin = datetime.datetime(2020, 12, 31)

# Descargar datos de acciones de Apple
df_api = web.DataReader("AAPL", "yahoo", inicio, fin)

print(df_api.head())


#Editar filas y columnas

# Agregar una nueva columna
df["País"] = ["España", "Panamá", "Perú"]

# Eliminar una columna
df.drop("Ciudad", axis=1, inplace=True)

# Eliminar una fila
df.drop("Fila2", inplace=True)

print(df)
