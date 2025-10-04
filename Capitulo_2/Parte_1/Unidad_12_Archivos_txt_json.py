# =======================================
# ARCHIVOS TXT: CREAR Y LEER
# =======================================
# Un TXT es un archivo de texto normal. Sirve para guardar datos 
# simples como listas, notas o registros.
# =======================================

# Creamos un archivo llamado "datos.txt" y escribimos dentro de él
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este es un archivo de texto\n")
    archivo.write("Se puede guardar cualquier cosa como texto\n")
    archivo.write("Por ejemplo: 123, 456, 789\n")

# Ahora leemos el contenido del archivo
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("\nContenido de datos.txt:")
    print(contenido)













# =======================================
# ARCHIVOS JSON: CREAR Y LEER
# =======================================
# Un JSON guarda información estructurada 
# (parecido a listas y diccionarios en Python).
# Se usa mucho en aplicaciones web y móviles.
# =======================================

import json

# Creamos un diccionario (parecido a la idea de JSON)
persona = {
    "nombre": "Ana",
    "edad": 20,
    "cursos": ["Python", "Matemáticas", "Inglés"]
}

# Guardamos el diccionario en un archivo JSON
with open("persona.json", "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, indent=2, ensure_ascii=False)

# Ahora leemos el archivo JSON
with open("persona.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print("\nContenido de persona.json (cargado en Python):")
    print(datos)
