#Unidad 37: Ordenación de datos

#Comprobar si hay datos faltantes
import pandas as pd
import numpy as np   # si usas np.nan en tus datos

import numpy as np

# 1.Crear un DataFrame con valores faltantes (NaN)
datos = {
    "Nombre": ["Ana", "Luis", "Carlos", "Marta"],
    "Edad": [23, np.nan, 29, 40],
    "Ciudad": ["Madrid", "Panamá", None, "Quito"]
}


df2 = pd.DataFrame(datos)
print(df2)

# Comprobar valores faltantes
print(df2.isnull())


# 2.Eliminar o sustituir valores faltantes

# Eliminar filas con valores faltantes
df_sin_na = df2.dropna()

# Sustituir valores faltantes por un valor fijo
#df_relleno = df2.fillna("Desconocido")

# Sustituir por la media de la columna
df_media = df2.fillna(df2.mean(numeric_only=True))

print(df_media)


# 3. Ordenar datos

# Ordenar por edad
df_ordenado = df2.sort_values(by="Edad")
print(df_ordenado)


# 4. Estadísticas descriptivas

print("Media:", df2["Edad"].mean())
print("Mediana:", df2["Edad"].median())
print("Varianza:", df2["Edad"].var())
print("Desviación estándar:", df2["Edad"].std())



# 5. Visualización de datos

import matplotlib.pyplot as plt

# Histograma
df2["Edad"].dropna().hist()
plt.title("Histograma de Edad")
plt.show()

# Diagrama de caja (boxplot)
df2.boxplot(column="Edad")
plt.title("Diagrama de Caja de Edad")
plt.show()

# Diagrama de dispersión
plt.scatter(df2.index, df2["Edad"])
plt.title("Diagrama de Dispersión de Edad")
plt.show()
