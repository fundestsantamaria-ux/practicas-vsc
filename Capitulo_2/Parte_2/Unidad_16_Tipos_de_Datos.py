# ====================================
# La Unidad 12 trata sobre tipos de datos de conjuntos en 
# Python (set), sus propiedades y operaciones.
# ====================================


#=============================
# EJEMPLO DE CONJUNTOS (SET)
#=============================

#numeros = set([1, 2, 2, 3])  
#print(numeros)  # {1, 2, 3}
# Los conjuntos eliminan automáticamente los valores duplicados






# Crear un conjunto con números repetidos
numeros = {1, 2, 2, 3, 4, 4, 5}

# Los conjuntos eliminan automáticamente los valores duplicados
print("Conjunto sin duplicados,:", numeros)  # Resultado: {1, 2, 3, 4, 5}

# Verificar si un número está dentro del conjunto con "in"
print(3 in numeros)  # True, porque el 3 está en el conjunto

# El operador "in" revisa si el número 3 está dentro del conjunto.

print(10 in numeros) # False, porque el 10 no está en el conjunto














###########



# Crear dos conjuntos con frutas
frutas1 = {"manzana", "pera"}
frutas2 = {"pera", "naranja"}

# Unión: junta todas las frutas sin repetir
print("Unión:", frutas1 | frutas2)   # {'manzana', 'pera', 'naranja'}

# '|' es un operador de conjuntos.
# Une ambos conjuntos y quita duplicados.
# {'manzana', 'pera', 'naranja'}

# Intersección: solo muestra lo que tienen en común
print("Intersección:", frutas1 & frutas2)  # {'pera'}

# '&' es otro operador de conjuntos.
# Solo muestra los elementos que están en los dos conjuntos.
# {'pera'}