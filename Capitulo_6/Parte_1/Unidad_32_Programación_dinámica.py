#La programación dinámica es una técnica para resolver problemas complejos.
#Se basa en resolver subproblemas, guardar sus resultados y reutilizarlos.

#Evita recalcular las mismas cosas una y otra vez.
#Ejemplos: Fibonacci, mochila, caminos más cortos.

#Consejos
#Úsalo cuando hay subproblemas superpuestos. Nos rferimos a problemas que se repiten.
#Pregúntate: ¿puedo dividir mi problema en partes más pequeñas que se repiten?
#En vez de calcular lo mismo varias veces, se guarda los resultados para ser muchoos más eficiente.

#Piensa: ¿ya resolví esto antes?

#Hay dos enfoques:
#Top-down (memorizacion) Comienza desde el problema grande y lo divide en subproblemas. Se almacena los resultados.
#Bottom-up (tabulación) Comienza desde los subproblemas más pequeños y construye la solución hacia arriba.

#Ejemplo en la vida real
#Planear un viaje optimizando costo/tiempo.
#Calcular el mínimo gasto en una serie de compras.



#=====================
#Ejemplo 1: Fibonacci con DP (bottom-up)

# Definimos una función llamada fibonacci_dp que calcula el n-ésimo número de Fibonacci
# utilizando Programación Dinámica (almacenando resultados intermedios en una lista).
def fibonacci_dp(n):
    # Creamos una lista que almacenará los valores de Fibonacci.
    # Comienza con los dos primeros números: fib[0] = 0 y fib[1] = 1.
    # Luego se añaden (n-1) ceros para tener espacio hasta fib[n].
    fib = [0, 1] + [0] * (n - 1)
    
    # Empezamos desde el índice 2 hasta n, calculando cada número
    # como la suma de los dos anteriores.
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    # Al final, devolvemos el valor de Fibonacci en la posición n.
    return fib[n]

# Probamos la función calculando el Fibonacci de 10
print("Fibonacci(10):", fibonacci_dp(10))

