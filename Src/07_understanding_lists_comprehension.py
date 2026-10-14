"""
    Una list comprehension combina 
    el for loop y creación de nuevos elementos
    en una sola linea y automáticamente agrega
    cada nuevo elemento a la lista, es decir,
    sin utilizar el método append.
"""
squares = [value**2 for value in range (0,11)]
print(squares)