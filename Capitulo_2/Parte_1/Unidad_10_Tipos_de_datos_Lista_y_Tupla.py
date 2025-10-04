#Unidad 10. Tipos de datos: Lista y Tupla
# ===============================
# LISTAS EN PYTHON 
# ===============================
# Una LISTA es una colección ordenada de elementos.
# - Puede contener números, texto o mezclarlos.
# - Es MUTABLE: se puede modificar después de crearla.

# Creamos una lista de frutas (tipo string).
frutas = ["manzana", "banana", "pera",]


# Mostramos la lista completa.
#print("Lista de frutas:", frutas)

# Accedemos al primer elemento (índice 0).
#print("Primera fruta:", frutas[0])

# Cambiamos el valor en la posición 1 (banana -> naranja).
#frutas[1] = "Uva"

# Mostramos la lista luego de la modificación.
#print("Lista después de cambiar banana:", frutas)

# Agregamos una fruta nueva al final de la lista usando append().
#frutas.append("kiwi")
#frutas.append("piña")
#frutas.append("maracuya")

# Ahora la lista tiene 4 elementos.
#print("Lista con nueva fruta:", frutas)

#frutas[3] = "fresas"







# ===============================
#---------Ejemplo 2
# ===============================
# TUPLAS EN PYTHON
# ===============================
# Una TUPLA también es una colección ordenada de elementos,
# pero es INMUTABLE: no se puede modificar después de creada.

# Creamos una tupla con coordenadas de un punto en un mapa.

coordenadas = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Mostramos toda la tupla.
print("Coordenadas:", coordenadas)

# Accedemos al primer valor (posición 0).
print("LLamado al valor X :", coordenadas[5])

# Accedemos al segundo valor (posición 1).
#print("Valor :", coordenadas[0])

# Intentar modificar un valor da error.
#coordenadas[0] = 50  #  Esto no está permitido.





vegetales = ["lechuga", "tomate", "cebolla", "zanahoria"]

for i in range(len(vegetales)):
    print("Vegetal en posición", i, "es", vegetales[i])

proteinas = ("pollo", "pescado", "huevos", "tofu")

while i in range(len(proteinas)):
    print("Proteina en posición", i, "es", proteinas[i])
    i += 1