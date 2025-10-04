# Que son las busquedas secuenciales?
# La búsqueda secuencial es un algoritmo simple para encontrar un elemento en una lista.

# Funciona revisando cada elemento de la lista uno por uno hasta encontrar el elemento buscado
# o hasta que se hayan revisado todos los elementos.

# Es fácil de implementar pero puede ser ineficiente para listas grandes.
# La complejidad temporal en el peor de los casos es O(n), donde n es el número de elementos en la lista.



# Tenemos una lista de números
numeros = [10, 20, 30, 40, 50]

# Queremos buscar el número 30
buscado = 100

# Recorremos la lista elemento por elemento
encontrado = False  # una bandera para saber si lo hallamos
for num in numeros:
    if num == buscado:
        encontrado = True
        break  # detenemos la búsqueda porque ya lo encontramos

# Mostramos el resultado
if encontrado:
    print(f"El número {buscado} está en la lista.")
else:
    print(f"El número {buscado} NO está en la lista.")
    # Explicación de f" dentro del print:
    # La f antes de las comillas indica que es una f-string (cadena formateada).
    # Permite insertar expresiones dentro de llaves {} que se evaluarán en tiempo de ejecución.
    # En este caso, {buscado} se reemplazará por el valor de la variable buscado.
    # print("El numero", buscando, "esta en la lista.")  # otra forma sin f-string

# Resultado: El número 30 está en la lista.
# Probamos con un número que no está
#buscado = 25