#---------Ejemplo 2

# ===============================
# DICCIONARIOS BÁSICOS
# ===============================
# Vamos a ver cómo CAMBIAR y AGREGAR información en un diccionario.

# Creamos un diccionario simple con datos de una mascota.
mascota = {
    "nombre": "Luna",
    "animal": "perro",
    "edad": 3
}

# Mostramos el diccionario original.
print("Diccionario original:", mascota)

# -------------------------------
# CAMBIAR UN VALOR
# -------------------------------
# Cambiamos la edad de la mascota (de 3 a 4).

mascota["animal"] = "caballo"

# -------------------------------
# AGREGAR UN NUEVO DATO
# -------------------------------
# Agregamos una nueva clave llamada "color".
mascota["color"] = "blanco"

# -------------------------------
# MOSTRAR RESULTADOS
# -------------------------------
print("Diccionario actualizado:", mascota)

# Ahora imprimimos cada dato de forma clara.
print("Nombre:", mascota["nombre"])
print("Tipo de animal:", mascota["animal"])
print("Edad:", mascota["edad"])
print("Color:", mascota["color"])