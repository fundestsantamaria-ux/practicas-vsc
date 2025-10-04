rd16 = {}

def funcion_rd(nombre, edad, pais, vehiculo, ID):
    return {
        "nombre": nombre,
        "edad": edad,
        "pais": pais,
        "vehiculo": vehiculo,
        "ID": ID

    }

p1 = funcion_rd("Jamil Guzman", 35, "Colombia", "Subaru", 246810)
p2 = funcion_rd("Melvin Garcia", 28, "Brasil", "Kia", 135792)   
p3 = funcion_rd("Randy Serra", 45, "Venezuela", "Honda", 112233)   
p4 = funcion_rd("Alexa Rodriguez", 25, "Peru", "Mazda", 445566)
p5 = funcion_rd("Josias Peguero", 32, "Estados Unidos", "Ford", 778899)
p6 = funcion_rd("Erick Caraballo", 29, "Chile", "Chevrolet", 998877)
p7 = funcion_rd("Francisco Gabriel", 31, "Argentina", "Toyota", 554433)


print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)