# Diccionario simple
alien_0 = {"color": "green", "points": 5}

# Diccionario vacío
alien_1 = {}

# El diccionario más simple
alien_2 = {"color": "verde"}

# Accesar a los elementos de un diccionario
print(f"Tu alien 0 es de color: {alien_0['color'].upper()}")
print(f"Si desvives al alien 0 se te otorgan: {alien_0['points']}")

# Agregar elementos a un diccionario
print("\nAgregando elemenetos al dict")
alien_0["x_position"] = 25
alien_0["y_position"] = 0

print(alien_0)

# Como modifiar el valor de un diccionario
print("\nModificando elementos del dict")
alien_0["y_position"] = 80
print(alien_0)

# Eliminando un elenmento de un diccionario
print("\nEliminando elemenetos del dict")
del alien_0["points"]
print(alien_0)

# Diccionarios para objetos (elementos) similares
favorite_languages = {
    "jen": "python", 
    "sarah": "c", 
    "eduard": "ruby", 
    "phill": "python"
}

# Looping though all key-values pairs
# Looping a través de todos los pares llave - valor
user_0 = {
    "username": "Charly",
    "firstname": "Tovar",
    "lastname": "García",
    "age": 34,
    "birthday": "6-feb"
}

print("\nLooping a través de los pares llave-valor")
for key, value in user_0.items():
    print("Key:", key)
    print("Value:", value)

print("\nLooping a través de las llaves")
for key in user_0.keys():
    print("Key:", key)

print("\nLooping a través de los valores")
for value in user_0.values():
    print("Value:", value)