print("Funciones creadas por el usuario")
# Las funciones
def Mi_lista():
    amigos=["Homero", "Paty", "Lety"]
    for sanchez in amigos:
        print(sanchez)
        
def Mi_tupla():
    animales=("Perro", "Gato", "Pajaro")
    for mascotas in animales:
        print(mascotas)
        
def Mi_conjunto():
    arcoiris={"Rojo", "Naranja", "Amarillo"}
    for colores in arcoiris:
        print(colores)
        
def Mi_diccionario():
    alumno={
        "Num": 1099,
        "Nombre": "Santiago",
        "Edad": 17,
    }
    print(alumno)
# Llamadas a funciones
Mi_lista()
Mi_tupla()
Mi_conjunto()
Mi_diccionario()