# NESTING

# Lista de diccionarios
covenant_elite = {"name": "elite", "color": "blue", "points": 10, "shield": True}
covenant_jackal =  {"name": "jackal", "color": "gray", "points": 6, "shield": True}
covenant_grunts =  {"name": "grunts", "color": "orange", "points": 3, "shield": False}

# Nesting de Lista de Diccionarios
covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

print("Looping")
# Looping though the list
for covenant in covenants:
    print(covenant)

# Vamos a crear una flotilla de enemigos (Covenant)
covenants_fleet = []
for _ in range(2):
    covenants_fleet.append(covenant_elite)

for _ in range(5):
    covenants_fleet.append(covenant_jackal)

for _ in range(20):
    covenants_fleet.append(covenant_grunts)

print("\n Flotilla")
print(covenants_fleet)

# Nesting: Una lista en un diccionario
# Menú
tacos = {
    "tortillas": ["maiz", "harina"],
    "guisos": ["bistec", "tripa", "pastor"]
}

print(f"\nTu has ordenado unos tacos de {tacos['guisos'][0]}")
print(f"En tortillas de {tacos['tortillas'][1]}")

# Nesting: Diccionarios en Diccionarios
# Menú de usuarios
user = {

    "charly": {
        "firstname": "Carlos",
        "middlename": "Antonio",
        "lastname": "Tovar Garcia",
        "Location": "México",
        "age": 34
    },
    "MrRed": {
        "firstname": "Jose",
        "middlename": "Lizandro",
        "lastname": "Villareal Martínez",
        "Location": "México",
        "age": 18
    }
}

# Looping de diccionarios en diccionarios
for user, user_info in user.items():
    fullname = f"{user_info['firstname']} {user_info["middlename"]} {user_info["lastname"]}"
    location = user_info["Location"]
    age = user_info["age"]
    print(f"\n\nEl nombre completo de {user} es:")
    print(fullname)
    print(f"\nLa ubicación de {user} es:")
    print(location)
    print(f"\nLa edad de {user} es:")
    print(age)