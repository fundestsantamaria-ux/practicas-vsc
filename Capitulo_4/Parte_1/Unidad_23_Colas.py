#======================
# Colas en Python
#======================
# Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out),
# lo que significa que el primer elemento en entrar es el primero en salir.
# Imagina una fila en un banco: la primera persona en llegar es la primera en ser atendida.
# Operaciones básicas de una cola:

# enqueue: agregar un elemento al final de la cola.
# dequeue: eliminar y devolver el primer elemento de la cola.
# peek: ver el primer elemento sin eliminarlo (no siempre se implementa).








# Importamos deque para crear colas fácilmente
from collections import deque

# Creamos una cola vacía
cola = deque()

# Personas llegan a la fila (encolar)
cola.append("Ana")   # Ana llega primero
cola.append("Luis")  # Luis llega después
cola.append("Marta") # Marta llega al final

print("Cola actual:", cola)  
# Resultado: deque(['Ana', 'Luis', 'Marta'])

# Atendemos al primero en la fila (desencolar)
primero = cola.popleft()  
print("Atendiendo a:", primero)  
# Resultado: Atendiendo a: Ana

print("Cola después de atender:", cola)  
# Resultado: deque(['Luis', 'Marta'])

# Atendemos al siguiente
siguiente = cola.popleft()
print("Atendiendo a:", siguiente)  
# Resultado: Atendiendo a: Luis

print("Cola final:", cola)  
# Resultado: deque(['Marta'])


#======================

# Creamos una lista vacía que usaremos como cola
cola= []

#Personas llegan a la fila (encolar)
cola.append("Genesis Beltre")    # llega primero
cola.append("Carlos Efrain")   #  llega después
cola.append("Erick Caraballo")  # llega al final

print("Cola actual:", cola)
# Resultado: ['Ana', 'Luis', 'Marta']

# Atendemos al primero en la fila (desencolar)
primero = cola.pop(0)   # quitamos el primer elemento
print("Atendiendo a:", primero)
# Resultado: Atendiendo a: Ana

print("Cola después de atender:", cola)
# Resultado: ['Luis', 'Marta']
