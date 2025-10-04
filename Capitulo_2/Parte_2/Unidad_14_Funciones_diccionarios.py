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
dic = {"nombre": "Ana", 
       "edad": 20, 
       "curso": "Python"
}

#Clave, valor
print(dic.keys())      # -> dict_keys(['nombre', 'edad', 'curso'])
print(dic.values())    # -> dict_values(['Ana', 20, 'Python'])
print(dic.items())     # -> dict_items([('nombre', 'Ana'), ('edad', 20), ('curso', 'Python')])

print(dic.get("nombre"))   # -> Ana
print(dic.pop("edad"))     # -> 20
print(dic.popitem())       # -> ('curso', 'Python')
dic.clear()
print(dic)                 # -> {}





#============================================

# Creamos un diccionario de ejemplo
dic = {"nombre": "Ana", 
       "edad": 20, 
       "curso": "Python",
}

# -------------------------------------------------------------------
# | Método       | ¿Qué hace?                                          | Ejemplo de uso | Resultado en este caso |
# -------------------------------------------------------------------

#Clave, valor

# keys() → Muestra todas las claves del diccionario
print(dic.keys())      
# Resultado: dict_keys(['nombre', 'edad', 'curso'])

# values() → Muestra todos los valores del diccionario
print(dic.values())    
# Resultado: dict_values(['Ana', 20, 'Python'])

# items() → Muestra pares (clave, valor)
print(dic.items())     
# Resultado: dict_items([('nombre', 'Ana'), ('edad', 20), ('curso', 'Python')])

# get(clave) → Busca un valor por su clave (no da error si no existe)
print(dic.get("nombre"))   
# Resultado: Ana

# pop(clave) → Elimina la clave indicada y devuelve su valor
print(dic.pop("edad"))     
# Resultado: 20  (además elimina "edad" del diccionario)

# popitem() → Elimina el último elemento agregado
print(dic.popitem())       
# Resultado: ('curso', 'Python')

# clear() → Borra todos los elementos del diccionario
dic.clear()
print(dic)                 
# Resultado: {}
