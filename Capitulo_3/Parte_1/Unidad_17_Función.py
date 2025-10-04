#=========================================
#¿Qué es una función?
#=========================================
#Una función es un bloque de código que se puede reutilizar.

#Se usa para organizar mejor el programa, evitar repetir
# código y hacerlo más fácil de mantener.
#=========================================

#Tipos de funciones en Python
#Funciones incorporadas (built-in) → Vienen listas en Python. 
#Ejemplo: print(), len(), type().

#Funciones definidas por el usuario → Las que tú mismo creas con def.

#Cómo definir una función
#Para definir una función se usa la palabra reservada def,

#=========================================

#def saludar(nombre):
    #bloque de código
    #print("Hola desde la función", nombre)
    #return valor  # opcional
    #print("Esto no se ejecuta porque está después del return")

    
#llamado = saludar("Erick")  # Llamar a la función    
#print("Hola, Bienvenidos todos!!!")  

#=========================================





#Ejemplo de función que suma dos números
#def sumar(a, b):
    #resultado = a - b
    #print("Dentro de la función, el resultado es:", resultado) 
    #return resultado

#No se ejecuta nada después del return
    #print("Esto no se ejecuta porque está después del return")
    #hola = "Hola"
    #return hola


    


#Llamar a la función
#suma = sumar(30, 5)      
#print("El resultado es:", suma)  # -> La suma es: 8



#def restar(a, b):
    #resultado = a - b
    #print("Dentro de la función, el resultado es:", resultado) 
    #return resultado
    #print("Esto no se ejecuta porque está después del return")  







#=========================================
#Otra forma de llamar a la función directamente en print

#print("La suma es:", sumar(10, 20))  # -> La suma es: 30
#=========================================






# Definimos una función que imprime un saludo
#Ejemplo 1: Función sin parámetros
#def saludar():
    #print("Hola, bienvenidos a la clase de Python")

# Llamamos a la función
#saludar()  
# Resultado: Hola, bienvenidos a la clase de Python
#=========================================






################################
# Ejemplo 2: Función con parámetros
################################

# Definimos una función que recibe un nombre y saluda
#def saludar_nombre(nombre):
    
    #print("Hola,", nombre)

# Llamamos a la función pasando un valor
#saludar_nombre("Ana")   # Resultado: Hola, Ana
#saludar_nombre("Luis")  # Resultado: Hola, Luis

#========================================

#Ejemplo 3: Función que devuelve un resultado con return
# Definimos una función que suma dos números

#def sumar(a, b,):  # Parámetros con valor por defecto
    #return a - b


# Guardamos el resultado en una variable
#resultado = sumar(4, 6)
#print("La suma es:", resultado)  # Resultado: La suma es: 10
#=========================================