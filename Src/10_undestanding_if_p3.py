guisos = ["Salsa verde", "deshebrada", "nopales"]

if "salsa verde" in guisos:
    print("hay salsa verde")
elif "deshebrada" in guisos:
    print("hay deshebrada")
elif "guiso especial" in guisos:
    print("hay guiso especial")


# Lista vacía
guisos_2 = ["salsa verde", "picadillo", "asado"]

if guisos_2:
    for guiso in guisos_2:
        print(guiso)
else:
    print("No hay guisos")

# 
guisos_disponibles = ["salsa verde", "deshebrada", "picadillo", "asado"]
guisos_a_ordenar = ["barbacoa", "deshebrada", "cabrito"]

for guiso in guisos_a_ordenar:
    
    if guiso in guisos_disponibles:
        print(f"Ordenaste {guiso}: Si hay de ese guiso")
    else:
        print(f"Ordenaste {guiso}: Una disculpa, no tenemos ese guiso")

print("Final")