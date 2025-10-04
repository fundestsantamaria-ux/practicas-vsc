#Qué es el enfoque Greedy (Avaro) en algoritmos?
#El enfoque Greedy es una estrategia algorítmica que toma decisiones basadas en la mejor opción 
# disponible en cada paso, sin considerar las consecuencias futuras. La idea es construir una solución 
# paso a paso, eligiendo la opción que parece ser la mejor en ese momento.

#Conceptos clave
#Se basa en tomar la mejor decisión local en cada paso, esperando que eso lleve a la mejor solución global.
#No siempre da la solución óptima en todos los problemas, pero funciona en muchos casos.

#Ejemplos típicos: cambio de monedas, selección de actividades, Huffman coding.

#Consejos
#Úsalo cuando:
#El problema tiene la propiedad de subestructura óptima (resolver partes pequeñas ayuda al todo).
#Existe la propiedad de elección Greedy (la mejor elección local lleva a la mejor global).

#Siempre pregunta: ¿Lo que es mejor ahora garantiza lo mejor al final?

#Ejemplo en la vida real
#Escoger las monedas más grandes primero para pagar.
#Organizar actividades escogiendo las que terminan más pronto.


#=====================
#Ejemplo de algoritmo Greedy: Problema del cambio de monedas

# Problema: dar cambio de 63 usando las monedas disponibles [25, 10, 5, 1]
# Estrategia Greedy: siempre usar la moneda más grande posible.

#Solo es un enfoque y se ajusta a la solucion optima en este caso particular

def cambio_greedy(cantidad, monedas):
    resultado = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)
    return resultado

monedas = [25, 10, 5, 1]
print("Cambio de 63:", cambio_greedy(63, monedas))
# Explicación: elige 25 -> 25 -> 10 -> 1 -> 1 -> 1
# Salida: [25, 25, 10, 1, 1, 1]


#No es la solucion eptima para todos los casos
#Por ejemplo, para dar cambio de 30 con monedas [25, 20, 5, 1], el enfoque Greedy daría [25, 5]

#Se aplica en problemas como:
#Toma de decisiones (ej. rutas más cortas).
#Optimización de recursos (ej. asignación de tareas).
#Compresión de datos (ej. codificación Huffman).
#Planificación (ej. selección de actividades).

#Recuerda:
#El enfoque Greedy es poderoso pero no infalible.
#Evalúa si es adecuado para tu problema antes de usarlo.
