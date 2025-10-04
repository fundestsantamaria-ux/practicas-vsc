# Que es una pila?
# Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out),
# lo que significa que el último elemento en entrar es el primero en salir.
# Imagina una pila de platos: el último plato que pones en la pila es el primero que
# vas a sacar cuando necesites uno.
# Operaciones básicas de una pila:

# push: agregar un elemento a la cima de la pila.
# pop: eliminar y devolver el elemento en la cima de la pila.
# peek: ver el elemento en la cima sin eliminarlo (no siempre se implementa).

#ejemplo de peek
#peek = pila.peek[-1]


# Creamos una lista vacía que usaremos como pila
pila = []

lista_rd = []


# Agregar elementos a la pila (apilar)
pila.append("A")
lista_rd.append("A")


pila.append("B")
pila.append("C")
pila.append("D")
pila.append("E")
pila.append("F")
print("Pila actual:", pila)  # ['A', 'B', 'C']

# Sacar el último elemento (desapilar)
ultimo = pila.pop()

#ver = pila[-1]
#print("Elemento en la cima (peek):", ver)  # 'B'    

print("Elemento eliminado:", ultimo)  # 'C'
print("Pila después de pop:", pila)   # ['A', 'B']

# Sacar otro elemento
#otro = pila.pop()
#print("Otro elemento eliminado:", otro)  # 'B'
#print("Pila final:", pila)               # ['A']