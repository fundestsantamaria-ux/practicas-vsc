# ¿Qué es una función de recursión?
# Recursión es una función que se llama a sí misma

# Una función recursiva es una función que se llama a sí misma para resolver un problema

# La función se llama a sí misma.
# Siempre debe tener un caso base para detenerse.






#Ejemplo 1: Factorial fácil
# Función recursiva para calcular el factorial
#def factorial(n):
    # Caso base: cuando n es 1, se detiene
    #if n == 1:
        #return 1
    # Llamada recursiva: multiplica n por el factorial de (n-1)
    #return n * factorial(n - 1)

# Ejemplo

#print(factorial(3))  # 3 * 2 * 1 = 6
#print(factorial(4))
#print(factorial(5))
#print(factorial(6))






# EL ORDEN IMPORTA A LA HORA DE OPERAR
######################################


#Ejemplo 2: Contar hacia atrás
# Función recursiva que imprime números hacia atrás
def cuenta_atras(n):
    if n == 0:  # Caso base
        print("¡Despegue!")
    else:
        print(n)
        cuenta_atras(n - 1)  # Llamada recursiva


# Ejemplo
#cuenta_atras(-10)




