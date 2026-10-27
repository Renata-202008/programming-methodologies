# Input - Sirve para realizar entradas de usuario
"""
    Método Build-in input

    input(argumento) - argumento (str): mensaje al usurio -prompt o instrucciones-

    input retorna un string
"""

user_welcome = """

        Bienvenidos al Sistema Creador de Nombre Completo
                    by Renata Marreros

Universidad Polítecnica de Victoria
"""
print(user_welcome)

print("\n\n\tBienvenidos al sistema creador de nombres completos".title())
print("\tby Renata M.M".title())
firstname = input("Escribe tu primer nombre: ")
middlename = input("Escribe tu segundo nombre: ")
lastname = input("Escribe tu apellido (Paterno / Materno):" )

fullname = f"{firstname} {middlename} {lastname}"
print(fullname.title())