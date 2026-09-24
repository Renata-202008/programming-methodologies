"""
    STRINGS
    
    Un string es de manera sencilla una serie de caracteres.
    En Python todo lo que se encuentre dentro de comillas simples
    '' o de dobles comillas "" es considerado un string. 
    
    Ejemplos:
        "Esto es un string"
        'Esto también es un string'
        'Le dije a un amigo, "Python" es mi lenguage favorito'
        "El lenguaje 'Python' lleva el nombre por Monty Python y no por la serpiente"
"""
name = "clase de proGRamación"
print(name)

print(name.title())

"""
    Un método es una acción que python
    puede realizar en un fragmento de datos
    o sobre una variable. 
    El punto . después de la variable
    seguida del método title() dice
    que se tiene que ejecutar el 
    método title de la variable name.

    Todos lo métodos van seguidos de
    paréntesis porque en ocasiones 
    necesitan información adicional
    para funcionar, lo cual iriía
    dentro del paréntesis. En esta ocasión
    el método .title() no requiere información
    extra para ejecutarse.

"""

# Concatenación de Caracteres

first_name = "renAta"
last_name = "maRrerOs"
full_name = first_name + " " + last_name
print(full_name)
print(first_name + " " + last_name)
print(full_name)
print("Que onda, "+full_name.title()+"!")

"""
    Whitespaces - Se refiere a cualquier caracter que no se imprime,
    es decir, un espacio, un tabulador y finales de línea. Los whitespaces
    se utilizan comúnmente para organizar las salidas, de tal manera que
    sea más amigable de leer o ver para los usuarios.
"""
print("\t\t\tPython")
print("Lenguajes: \nPython\nC\nJavascript")

programming_language = "     Python     "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

message = "Una fortaleza de Python es su Comunidad y sus alumnos de la upv"
message = 'Una fortaleza de "PYTHON" su facilidad de enteder'
print(message)