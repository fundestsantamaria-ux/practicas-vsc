#Que son las busquedas binarias?
#Es un algoritmo de busqueda que se utiliza para encontrar la posicion 
# de un elemento en una lista ordenada.

#El algoritmo funciona dividiendo repetidamente a la mitad el 
# rango de busqueda hasta que el elemento se encuentra o el rango de 
# busqueda se reduce a cero.

#La busqueda binaria es mucho mas eficiente que la busqueda
#  lineal, especialmente para listas grandes.


# Lista ORDENADA
numeros = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000 )

# Número que queremos buscar
Busqueda = 40000

# Límites
inicio = 0
fin = len(numeros) - 1

# Búsqueda binaria con while
while inicio <= fin:
    medio = (inicio + fin) // 2   # posición del medio
    if numeros[medio] == Busqueda:
        print("Encontrado en la posición:", medio)
        break
    elif numeros[medio] < Busqueda:
        inicio = medio + 1  # buscamos en la derecha
    else:
        fin = medio - 1     # buscamos en la izquierda

# Si no se encuentra
else:
    print("No encontrado")






#-----===========-------
#Con while: el ciclo se repite hasta que se cumpla la condición (inicio <= fin).

#Con for: tenemos que darle un número de repeticiones “máximo” 
# (aquí usamos len(numeros) por seguridad, aunque en realidad se necesitan 
# como mucho log₂(n) pasos).


#Se recomienda while porque se adapta mejor a este algoritmo.
#Sí se puede usar for, pero hay que limitar el número de pasos.