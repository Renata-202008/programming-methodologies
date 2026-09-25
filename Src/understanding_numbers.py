# Números
# Enteros 
# Sumar + 
# Restar -
# Multiplicar *
## Dividir /
## División entera //
# Potencias **n

print(2+3) 
print(3-1) 
print(2*3)
print(3/2)

print(3**2) #3^2
print(3**3) #3^3
print(10%2) # Módulo (mod)
age = 18
print(age)
name = "Renata Marreros"
print(name,age)

# Floats 
"""
    Python llama Floats a cualquier número
    con punto decimal
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# Imprimir la edad de alguien
age = 18 #Variable del tipo int
# message = "Renata tiene " + age + "años." (Error)
message = "Renata tiene " + str(age) + " años."
message_f = f"Renata tiene {age} años."
print(message)
print(message_f)


"""
    TypeError: Python no puede reconocer el tipo
    de información que se está utilizando.

    En este caso no se pueden concatenar 
    ints a string.
"""
print(type(age))
print(type(0.1))
print(type(message_f), type(1+5), type(1+0.5))
