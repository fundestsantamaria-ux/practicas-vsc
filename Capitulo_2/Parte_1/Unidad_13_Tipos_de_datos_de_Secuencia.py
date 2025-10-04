# ====================================
# LISTAS 2D EN PYTHON
# ====================================
# Una lista 2D es simplemente una lista que contiene otras listas.
# Podemos imaginarla como una "tabla" con filas y columnas.
#
# Ejemplo de una lista normal (1D):
# numeros = [1, 2, 3]
#
# Ejemplo de una lista 2D:
# matriz = [
#     [1, 2, 3],   <-- fila 0
#     [4, 5, 6],   <-- fila 1
#     [7, 8, 9]    <-- fila 2
# ]

#Matriz (2 filas x 3 columnas)

#[ 1   2   3 ]   ← Fila 0
#[ 4   5   6 ]   ← Fila 1
#  ↑   ↑   ↑
# Col0 Col1 Col2


# Aquí cada fila es una lista independiente.

# Creamos una lista 2D llamada "matriz".
matriz = [
    [1, 2, 3],   # fila 0
    [4, 5, 6],   # fila 1
    [7, 8, 9]    # fila 2
]

# ====================================
# ACCESO A ELEMENTOS
# ====================================
# Para acceder a un elemento necesitamos DOS índices:
# - El primero indica la FILA.
# - El segundo indica la COLUMNA.

# Accedemos al número en fila 0, columna 1.
print("Elemento en fila 0, columna 1:", matriz[0][0])  # valor 1

# Accedemos al número en fila 2, columna 2.
print("Elemento en fila 2, columna 2:", matriz[2][2])  # valor 9










#---------Ejemplo 2

# ================================
# LISTAS 2D (MATRICES) SIMPLIFICADO
# ================================
# Recordemos: una lista 2D es una lista que contiene otras listas.
# Se parece a una "tabla" de filas y columnas.


# Creamos una lista 2D (matriz de 3x3).

matriz = [
    [1, 2, 3],   # fila 0
    [4, 5, 6],   # fila 1
    [7, 8, 9]    # fila 2
]

# -------------------------------
# RECORRER LA MATRIZ
# -------------------------------
# Vamos a mostrar todos los valores de la matriz.
# Usamos dos bucles: uno para las filas y otro para las columnas.

print("Mostrando la matriz completa:")
for fila in matriz:        # Recorremos cada fila
    print(fila)            # Mostramos la fila completa


# -------------------------------
# MODIFICAR UN VALOR
# -------------------------------
# Cambiamos el número que está en la fila 1, columna 1.
# Recordemos: los índices empiezan en 0.
# matriz[fila][columna]
matriz[1][1] = 88  # cambiamos el número 5 por 99

# -------------------------------
# RESULTADO FINAL
# -------------------------------
print("Matriz después del cambio:")
for fila in matriz:
    print(fila)
