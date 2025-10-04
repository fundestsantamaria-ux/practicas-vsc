#Que es una tabla hash?
#Es una estructura de datos que implementa un tipo de dato abstracto 
# llamado mapa o diccionario.

#Una tabla hash asocia claves (keys) a valores (values).

#Permite almacenar y recuperar datos de manera eficiente.

#Utiliza una función hash para convertir la clave en un índice de un array.

#La función hash toma una clave y devuelve un número entero que representa 
# la posición en el array donde se almacenará el valor asociado a esa clave.

#Si dos claves diferentes generan el mismo índice, se produce una colisión.

#Existen varias técnicas para manejar las colisiones, 
# como el encadenamiento y la direccion abierta.

#Las tablas hash son muy eficientes para operaciones de búsqueda, 
# inserción y eliminación, con un tiempo promedio de O(1) para estas operaciones.

#Una tabla hash es una estructura de datos que guarda pares clave → valor.

#Permite buscar datos muy rápido (casi instantáneo).

#En Python, los diccionarios (dict) ya son tablas hash.


#-===-==-=-=-=-=-=-=-=-=-=-=-===

# Creamos una "tabla hash" usando un diccionario
#Clave = nombre= "", Valor = "" (edad)  ////// CLAVE    VALOR


#personas = {
    #"Josias Peguero": 40,
    #"Angel Bather": 31,
    #"Alexa Rodriguez": 25,
#}

# Buscar un valor usando su clave
#print("Edad de Josias :", personas["Josias Peguero"]) # X
#print("Edad de Angel ", personas["Angel Bather"])   # X
#print("Edad de Alexa:", personas["Alexa Rodriguez"]) # X

# Agregar un nuevo elemento
#personas["Pedro"] = 40
#print("Tabla hash actual:", personas)
# Eliminar un elemento
#del personas["Jesus"]


















#Ejemplo con colisión
# Creamos la tabla hash
tabla_hash = [[] for _ in range(10)]

def funcion_hash(clave):
    return len(clave) % 10

def insertar(clave, valor):
    indice = funcion_hash(clave)
    tabla_hash[indice].append((clave, valor))

def mostrar_tabla():
    for i, bucket in enumerate(tabla_hash):
        print(f"[{i}] → {bucket}")


# Insertamos elementos (Ana y Eva causan colisión)
insertar("Ana", 20)
insertar("Eva", 22)

# Mostramos la tabla hash, siguiendo tematica lamba
mostrar_tabla()
#======================