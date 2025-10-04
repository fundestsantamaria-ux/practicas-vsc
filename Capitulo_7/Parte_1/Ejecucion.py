#pip install pandas
#pip install numpy
#pip install matplotlib
#pip install matplotlib.pyplot


#=====================


# milib.py

def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido a mi librería."

def suma(a, b):
    return a + b


# main.py

from milib import saludo, suma  # Importo funciones específicas

print(saludo("Alex"))
print(suma(5, 7))
