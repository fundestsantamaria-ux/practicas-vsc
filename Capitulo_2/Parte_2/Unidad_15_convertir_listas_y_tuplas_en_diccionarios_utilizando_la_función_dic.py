# ====================================
# LISTAS Y TUPLAS COMO DICCIONARIOS
# ====================================
# Recordemos que un diccionario en Python es una 
# colección de pares clave-valor. Podemos crear diccionarios
# a partir de listas o tuplas 
#=====================================
# La función dict() en Python se utiliza para crear diccionarios. 
#=====================================




 # Listas de claves y valores
claves = ["nombre", "edad", "curso", "ciudad", "país"]
valores = ["Ana", 20, "Python", "Santo Domingo", "República Dominicana"]

# Convertimos listas a diccionario
dic = dict(zip(claves, valores))
print("Diccionario creado:", dic)

# Recorrer con bucle
for clave, valor in dic.items():
    print(clave, ":", valor)
