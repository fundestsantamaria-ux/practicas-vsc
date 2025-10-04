#Qué es un closure (cierre) en Python?
# Un closure es una función que recuerda el entorno en el que fue creada, incluso cuando se
# ejecuta fuera de ese entorno.

# Un closure puede acceder a variables de su entorno externo, incluso después de que ese entorno
# haya terminado su ejecución.

# Un closure se crea cuando una función interna (anidada) accede a variables de la función
# externa.

# Los closures son útiles para crear funciones con estado o para encapsular datos.
# Ejemplo de closure:




def contador():
    numero = 0  # variable de afuera

    def incrementar():
        nonlocal numero  # podemos cambiar la variable de afuera
        numero += 1
        return numero
    
    return incrementar  # devolvemos la función interna

# Creamos el closure
mi_contador = contador()

print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3
print(mi_contador())  # 4
print(mi_contador())  # 5 
print(mi_contador())  # 6
print(mi_contador())  # 7
print(mi_contador())  # 8
print(mi_contador())  # 9
print(mi_contador())  # 10

