# If statement
print("\nif statement")
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)


# El condicional o conditional
# El condicional es el corazón del if

# Condicional Verdadero
print("\nCondicional True")
truck = "ford"
print(truck == 'ford')

# Condicional Falso
print("\nCondicional False")
print(truck == 'audi')

# Distingue entre mayusculas y minusculas
print(truck == 'Ford'.lower())

# Condicional de Desigualdad 
print(truck!="audi") # Tiene que regresar true ya que si es diferente lo q trae la variable
print(truck!="ford") # False pq si esta ford en las variables


# Comparaciones númericas
print("\nComparaciones numéricas")
age = 34
print(age==34) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta")

# Conector menor que <
print("\nConectores < > <= >=")
age = 19
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Multiples condicionales
age_0 = 22
age_1 = 18
print("\nMultiple Conditions")
print("Operación AND")
print( age_0>=21 and age_1 >= 21) # False
print( age_0>=21 and age_1 >= 18) # True

print("Operación OR")
print( age_0>=21 or age_1 >= 21) # True
print( age_0>=23 or age_1 >= 21) # False

# ¿Como saber si un elemento esta en una lista?
food = ["chilaquiles", "flautas", "gorditas", "tamales"]
print("\n¿Nopales esta en la lista?")
print("nopales" in food) # False
print("\n¿Gorditas esta en la lista?")
print("gorditas" in food) # True

banned_user = ["andrew", "carolina", "David"]
user = "marie"
print("\n¿Marie no esta en la lista?")
print(user not in banned_user) # True