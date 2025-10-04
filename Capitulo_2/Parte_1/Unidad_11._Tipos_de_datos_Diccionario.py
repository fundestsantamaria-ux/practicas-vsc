# ===============================
# DICCIONARIOS EN PYTHON
# ===============================
# Un diccionario guarda datos en pares clave:valor.
# - La clave funciona como "etiqueta".
# - El valor es la información que se guarda.

# Creamos un diccionario con datos de una persona.
persona = {
    "nombre": "Zacarias Ferreira",
    "edad": 55,
    "ciudad": "SANTO Domingo",
    "Pais": "Republica Dominicana",
    "Profesión": "Cantante",
    "Estado Civil": "Unido",
    "Cedula": "0-1234545847-8",
    "Carros": ["Toyota", "Honda", "Ford"],
    "Hijos": {"Hijo1": "Juan", "Hijo2": "Pedro" }




}

# Mostramos el diccionario completo.

persona["Carros"] = ["Toyota", "Kia", "Porsche"]
print("Carros Modificados:", persona)

# Accedemos a valores usando las claves.
#print("Cedula", persona["Cedula"])
#print("Edad:", persona["nombre"])
#print("Ciudad:", persona["ciudad"])
print("Carros:", persona["Carros"])






#| Método       | ¿Qué hace?                                                | Ejemplo de uso      | Resultado                                      |
#| ------------ | --------------------------------------------------------- | ------------------- | ---------------------------------------------- |
#| `keys()`     | Muestra todas las **claves** del diccionario              | `dic.keys()`        | `dict_keys(['nombre', 'edad'])`                |
#| `values()`   | Muestra todos los **valores** del diccionario             | `dic.values()`      | `dict_values(['Ana', 20])`                     |
#| `items()`    | Muestra pares de **(clave, valor)**                       | `dic.items()`       | `dict_items([('nombre', 'Ana'), ('edad',20)])` |
#| `get(clave)` | Busca un valor por su **clave**. No da error si no existe | `dic.get("nombre")` | `"Ana"`                                        |
#| `pop(clave)` | Elimina el valor con esa **clave** y lo devuelve          | `dic.pop("edad")`   | `20` y elimina `"edad"` del diccionario        |
#| `popitem()`  | Elimina el **último elemento agregado**                   | `dic.popitem()`     | `('curso', 'Python')`                          |
#| `clear()`    | Borra **todos los elementos** del diccionario             | `dic.clear()`       | `{}` (diccionario vacío)                       |
#| `update()`   | Actualiza el diccionario con **otro diccionario**         | `dic.update({...})` | Agrega o modifica pares clave:valor            |


# Diccionario de ejemplo
dic = {"nombre": "Ana", "edad": 20, "curso": "Python"}

print(dic.keys())      # -> dict_keys(['nombre', 'edad', 'curso'])
print(dic.values())    # -> dict_values(['Ana', 20, 'Python'])
print(dic.items())     # -> dict_items([('nombre', 'Ana'), ('edad', 20), ('curso', 'Python')])

print(dic.get("nombre"))   # -> Ana
print(dic.pop("edad"))     # -> 20
print(dic.popitem())       # -> ('curso', 'Python')
dic.clear()
print(dic)                 # -> {}
