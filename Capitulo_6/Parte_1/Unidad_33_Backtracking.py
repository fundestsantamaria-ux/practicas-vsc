#El backtracking es una técnica algorítmica para resolver problemas de decisión, optimización y búsqueda.
#Técnica de búsqueda en profundidad: explora todas las posibilidades, retrocediendo cuando una no funciona.

#Usa una pila implícita de llamadas recursivas.

#Ejemplos: N-reinas, laberintos, sudoku.

#Consejos
#Es útil cuando hay que explorar múltiples opciones.
#Utilizar pilas y colas para gestionar estados.
#Aplica poda: descarta ramas imposibles antes de explorarlas.

#Ejemplo en la vida real
#Resolver un laberinto probando caminos.
#Hacer combinaciones posibles en un juego de mesa.

#=====================


# Función que verifica si es válido colocar una reina en la posición (fila, col)
def es_valida(tablero, fila, col):
    # Recorremos las filas anteriores para comprobar conflictos
    for i in range(fila):
        # Condiciones de amenaza:
        # 1. Si ya hay una reina en la misma columna
        # 2. Si hay una reina en la diagonal izquierda
        # 3. Si hay una reina en la diagonal derecha
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False  # No se puede colocar aquí
    return True  # Si no hay conflicto, la posición es válida

# Función recursiva que resuelve el problema de las N-Reinas
def resolver_n_reinas(n, fila=0, tablero=[]):
    # Caso base: si llegamos a la última fila, encontramos una solución
    if fila == n:
        print("Solución encontrada:", tablero)  # Mostramos la posición de cada reina
        return
    
    # Probamos todas las columnas de la fila actual
    for col in range(n):
        # Verificamos si se puede colocar una reina en (fila, col)
        if es_valida(tablero, fila, col):
            # Si es válido, seguimos con la siguiente fila
            # Se añade la columna a la lista "tablero"
            resolver_n_reinas(n, fila + 1, tablero + [col])

# Probamos con un tablero de 4x4 (clásico ejemplo)
resolver_n_reinas(4)
