"""
     TUPLAS 

     Las tuplas son listas de elementos que no cambian de tamaño.
     Las tuplas son listas inmutables.

     Se utilizan los paréntesis () para definir una tupla. (Se usan para optimizar espacio en la memoria)

     Ejemplo:

        Si tenemos un rectangulo (largo, ancho) que siempre va
        a tener cierto tamaño, podemos asegurar que sus dimensiones
        no va a cambiar si colocamos sus valores en una tupla.

    En las tuplas no se puede utilizar ningun metodo de las listas pq es inmutable
"""
dimensions = (200,50) # 200 de largo x 50 de ancho
print("tupla original: ", dimensions)

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que con una lista.
print(dimensions[0])
print(dimensions[1])
# print(dir(dimensions))

# Vamos a modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury"
names[1] = "mercury" # Modifica elementos de una lista
print(names)

# dimensions[0] = 90 # TypeError: 'tuple' object does not support item assignment (Las tuplas no se modifican)

# Looping trough a tuple
for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla,
    lo que si podemos hacer es cambiar 
    la asignación de una variable que 
    almacena una tupla.
"""
dimensions = (500,1000,20)
print("tupla original: ", dimensions)
"""
# Lista
dimensions_2 = [200,50]
print(dir(dimensions_2)) -- muestra los atrinutos y métodos de tu variable.

name = "charly"
print(dir(name))
"""

# Tipos de datos Booleanos
answer = True
print(answer)
#print(dir(answer))