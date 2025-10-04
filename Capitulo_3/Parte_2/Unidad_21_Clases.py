#Que son clases en Python?
# Una clase es una plantilla para crear objetos.

# Una clase define atributos
#  (características) y métodos (comportamientos) que los objetos

# Una clase es como un plano o molde que define
#  cómo se verá y cómo se comportará un objeto.

# Los objetos son instancias de una clase.

# Podemos pensar en una clase como un "tipo de dato" personalizado.

# Podemos crear múltiples objetos (instancias) a partir
#  de una misma clase.

# Ejemplo de clase:

#def: estamos definiendo un método.

#__init__: el nombre especial del constructor (Python lo reconoce así).
#self: representa al objeto que estamos creando.
#nombre, edad: son parámetros que debemos pasar al crear el objeto.

#=====================
# Sintaxis básica de una clase en Python
#class Mi_primera_clase:
#=====================



class Persona:
    # Atributos (características)
    #funcion 1 = __init__, sin embargo se denomina Steven
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad      # atributo de instancia

    # Métodos (comportamientos)
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear instancias (objetos) de la clase Persona
persona1 = Persona("Johan", 20)
persona2 = Persona("Wandrys", 19)

# Usar los métodos de las instancias
print(persona1.saludar())  # Hola, mi nombre es Johan y tengo 20 años.
print(persona2.saludar())  # Hola, mi nombre es Wandrys y tengo 19 años.


#=====================
# Ejemplo 2: Clase Perro

#Características:
#Comportamientos:

# Definimos una clase llamada Perro
class Perro:
    # Método para que el perro ladre
    def ladrar(self):
        print("¡Guau guau!")
    
    # Método para que el perro corra
    def correr(self):
        print("El perro está corriendo.")

# Creamos un objeto de la clase Perro
mi_perro = Perro()

# Usamos los métodos del objeto
mi_perro.ladrar()   # Muestra: ¡Guau guau!
mi_perro.correr()   # Muestra: El perro está corriendo.


#=====================
#¿Qué es self?

#En Python, cuando creamos una clase, los métodos dentro de la clase 
# siempre reciben como primer parámetro self.

#self representa al propio objeto que estamos usando.

#Gracias a self, cada objeto puede guardar y usar sus propios datos.

#Pensemos en self como el “yo” del objeto.