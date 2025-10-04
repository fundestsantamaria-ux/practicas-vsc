#Conceptos clave

#Estrategia: dividir el problema en subproblemas más pequeños, resolverlos recursivamente, y luego combinar las soluciones.
#Ejemplos clásicos: búsqueda binaria, mergesort, quicksort.

#Consejos
#Es ideal cuando el problema se repite en escalas más pequeñas.
#Pregúntate: ¿puedo partir mi problema en mitades iguales o más pequeñas?

#Ejemplo en la vida real
#Buscar un número en una agenda telefónica (abrir por la mitad → descartar mitad).
#Organizar un torneo eliminatorio.

#=====================
#Suma de arreglo con divide y vencerás

# Definimos una función llamada suma_dividir que recibe una lista de números
def suma_dividir(lista):
    # Caso base: si la lista tiene solo un elemento, se devuelve ese elemento
    if len(lista) == 1:
        return lista[0]
    
    # Calculamos el índice del medio de la lista
    medio = len(lista) // 2
    
    # Aplicamos recursión a la mitad izquierda de la lista
    izquierda = suma_dividir(lista[:medio])
    
    # Aplicamos recursión a la mitad derecha de la lista
    derecha = suma_dividir(lista[medio:])
    
    # Al final, sumamos los resultados de ambas mitades
    return izquierda + derecha

# Probamos la función con una lista de ejemplo
print("Suma:", suma_dividir([1, 2, 3, 4, 5]))




#=====================
#Divide y veceras se utiliza en algoritmos de ordenamiento como mergesort y quicksort 
#La temática de divide y vencerás es amplia y se aplica en muchos otros algoritmos y problemas.

#Recuerda:
#Divide y vencerás es una estrategia poderosa, pero no siempre es la mejor opción.
#Evalúa si es adecuado para tu problema antes de usarlo.