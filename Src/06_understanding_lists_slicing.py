players = ['charly', 'juan', 'iancarlo', 'lizandro']
print("Lista original: ", players)

# Slicing
print(players[0:2]) # ['charly', 'juan']

# El slicing me permite trabajar con un grupo 
# especifíco de una lista: al resultado se le conoce como 
# "un slice".

print(players[1:4]) # ['juan', 'iancarlo', 'lizandro']
print(players[:4]) # ['charly', 'juan', 'iancarlo', 'lizandro']
print(players[2:]) # ['iancarlo', 'lizandro']
print(players[-3:]) #['juan', 'iancarlo', 'lizandro']

# ['charly', 'juan', 'iancarlo', 'lizandro']
# Casos especiales 
print(players[1:6]) # ['juan', 'iancarlo', 'lizandro'] # En slicing no agrega valores al index
print(players[6:1]) # [] # Lista vacia pq no hay nada antes
print(players[:0]) # [] # Empieza desde cero y termina en 0

# Looping through a slice
print("\nLooping trough a slice")
students = ['charly', 'juan', 'iancarlo', 'lizandro']

# Slicing[::] Tarea
for student in students[2:4]: # Al poner [2:4] se hace un slice de los elementos que quiero de la lista
    print(f"El estudiante {student}, va a pasar la materia.")
print(students)

# ¿Cómo podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food # Es la misma lista -manera erronea de copiar una lista- 
 
# 3 maneras de copiar una lista
# Método 1 - utilizando slicing
my_friend_food_2 = my_food[:]

# Método 2 - utilizando el método de las listas .copy()
my_friend_food_3 = my_food.copy()

# Método 3 - utilizando el método build-in list()
my_friend_food_4 = list(my_food)
