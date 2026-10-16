# Manejo de Strings de python 
"""
Renata Valeria Marreros Moreno
2630582
IM 1-2
"""
"""
Resumen Ejecutivo
Un string en Python es un tipo de dato que permite almacenar texto, como nombres, 
correos electrónicos y contraseñas. 
Es inmutable, lo que significa que su contenido no puede modificarse directamente 
después de crearse. 
Entre sus operaciones básicas se encuentran concatenar textos, conocer su longitud ,
extraer subcadenas mediante índices y buscar patrones o caracteres. 
También permite reemplazar partes del texto utilizando el método replace(). 
Validar y normalizar los datos de entrada es importante para evitar errores, eliminar 
espacios innecesarios y mantener un formato consistente. 
"""
# Problem 1: Full name formatter (name + initials)
# Description: Normalize a person's full name, display it in Title Case, and generate the person's initials.

# Inputs:
# full_name (string): The person's full name.

# Outputs:
# Formatted name and initials.

# Validations:
# - The input cannot be empty.
# - The input must contain at least two words.

# Test Cases:
# 1. Normal: "juan carlos tovar" -> "Juan Carlos Tovar", "J.C.T."
# 2. Boundary: "Renata Marreros" -> "Renata Marreros", "R.M."
# 3. Error: "   " -> "Error: invalid input"

full_name = input("Enter your full name: ")

# Remove leading and trailing spaces
full_name = full_name.strip()

# Validate that the input is not empty
if len(full_name) == 0:
    print("Error: invalid input")

else:
    # Split the name into words and remove extra spaces
    name_parts = full_name.split()

    # Validate that the name contains at least two words
    if len(name_parts) < 2:
        print("Error: invalid input")

    else:
        # Format the full name
        formatted_name = " ".join(name_parts).title()

        # Generate the initials
        initials = ""

        for name_part in name_parts:
            initials += name_part[0].upper() + "."

        # Display the results
        print(f"Result: {formatted_name}")
        print(f"Initials: {initials}")

# Problem 2: Simple email validator (structure + domain)
# Description:
# Validate a basic email format and display its domain if valid.

# Inputs:
# email_text (string): The email address entered by the user.

# Outputs:
# "Valid email: true" or "Valid email: false"
# If valid, display "Domain: <domain_part>"

# Validations:
# - The email cannot be empty.
# - The email must contain exactly one '@'.
# - The domain must contain at least one '.'.
# - The email cannot contain spaces.

# Test Cases:
# 1. Normal: "user@example.com" -> Valid email: true
#    Domain: example.com
# 2. Boundary: "a@b.c" -> Valid email: true
#    Domain: b.c
# 3. Error: "user example.com" -> Valid email: false

email_text = input("Enter your email address: ")

# Remove leading and trailing spaces
email_text = email_text.strip()

# Validate that the email is not empty
if len(email_text) == 0:
    print("Valid email: false")

else:
    # Check the basic email conditions
    at_count = email_text.count("@")
    at_position = email_text.find("@")

    if (
        at_count == 1
        and " " not in email_text
        and "." in email_text[at_position + 1:]
    ):
        domain_part = email_text[at_position + 1:]

        print("Valid email: true")
        print(f"Domain: {domain_part}")

    else:
        print("Valid email: false")

# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
# Determine whether a phrase is a palindrome, ignoring spaces and uppercase or lowercase letters.

# Inputs:
# phrase (string): The phrase entered by the user.

# Outputs:
# "Is palindrome: true" or "Is palindrome: false"
# Display the normalized phrase.

# Validations:
# - The phrase cannot be empty.
# - The normalized phrase must contain at least three characters.

# Test Cases:
# 1. Normal: "Anita lava la tina" -> Is palindrome: true
# 2. Boundary: "a b a" -> Is palindrome: true
# 3. Error: "a " -> Error: invalid input

phrase = input("Enter a phrase: ")

# Remove leading and trailing spaces
phrase = phrase.strip()

# Normalize the phrase
normalized_phrase = phrase.lower().replace(" ", "")

# Validate the input
if len(normalized_phrase) < 3:
    print("Error: invalid input")

else:
    # Reverse the normalized phrase
    reversed_phrase = normalized_phrase[::-1]

    # Compare the original and reversed phrases
    is_palindrome = normalized_phrase == reversed_phrase

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")

# Problem 4: Sentence word stats (lengths and first/last word)
# Description:
# Analyze a sentence to count its words and identify the first,
# last, shortest, and longest words.

# Inputs:
# sentence (string): A sentence entered by the user.

# Outputs:
# Word count, first word, last word, shortest word, and longest word.

# Validations:
# - The sentence cannot be empty.
# - The sentence must contain at least one word.

# Test Cases:
# 1. Normal: "Python is very useful"
#    Word count: 4
#    First word: Python
#    Last word: useful
#    Shortest word: is
#    Longest word: Python

# 2. Boundary: "Hello"
#    Error: invalid input (only one word is not accepted)

# 3. Error: "   "
#    Error: invalid input

sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
sentence = sentence.strip()

# Validate the input
if len(sentence) == 0:
    print("Error: invalid input")

else:
    # Split the sentence into words
    words = sentence.split()

    # Validate that at least one word exists
    if len(words) == 0:
        print("Error: invalid input")

    else:
        # Count the words
        word_count = len(words)

        # Get the first and last words
        first_word = words[0]
        last_word = words[-1]

        # Initialize the shortest and longest words
        shortest_word = words[0]
        longest_word = words[0]

        # Find the shortest and longest words
        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word

            if len(word) > len(longest_word):
                longest_word = word

        # Display the results
        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

# Problem 5: Password strength classifier
# Description:
# Classify a password as weak, medium, or strong according
# to its length and character types.

# Inputs:
# password_input (string): The password entered by the user.

# Outputs:
# "Password strength: weak"
# "Password strength: medium"
# "Password strength: strong"

# Validation:
# - The password cannot be empty.

# Rules:
# - Weak: Fewer than 8 characters.
# - Medium: At least 8 characters and contains letters or digits,
#   but does not meet all strong password requirements.
# - Strong: At least 8 characters, one uppercase letter,
#   one lowercase letter, one digit, and one special character.

# Test Cases:
# 1. Normal: "Hello123!" -> Password strength: strong
# 2. Boundary: "Abc12345" -> Password strength: medium
# 3. Error: "" -> Error: invalid input

password_input = input("Enter a password: ")

# Validate the input
if len(password_input) == 0:
    print("Error: invalid input")

else:
    # Initialize character flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Check each character
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    # Classify password strength
    if len(password_input) < 8:
        password_strength = "weak"

    elif has_upper and has_lower and has_digit and has_symbol:
        password_strength = "strong"

    else:
        password_strength = "medium"

    # Display the result
    print(f"Password strength: {password_strength}")

# Problem 6: Product label formatter (fixed-width text)
# Description:
# Generate a product label with exactly 30 characters.
# Short labels are padded with spaces; long labels are truncated.

# Inputs:
# product_name (string): The product name.
# price_value (string): The product price.

# Outputs:
# "Label: <exactly 30 characters>"

# Validations:
# - The product name cannot be empty.
# - The price must be a valid positive number.

# Test Cases:
# 1. Normal: "Mouse", "25.50"
# 2. Boundary: "Pen", "1"
# 3. Error: "Laptop", "-10"

product_name = input("Enter the product name: ").strip()
price_value = input("Enter the product price: ").strip()

# Validate the product name
if len(product_name) == 0:
    print("Error: invalid input")

else:
    # Validate the price
    try:
        price_number = float(price_value)

        if price_number <= 0:
            print("Error: invalid input")

        else:
            # Convert the price to a string
            price_text = str(price_number)

            # Create the label
            label = f"Product: {product_name} | Price: ${price_text}"

            # Truncate or pad the label to exactly 30 characters
            label = label[:30]
            label = label.ljust(30)

            # Display the label and its length
            print(f'Label: "{label}"')
            print(f"Length: {len(label)}")

    except ValueError:
        print("Error: invalid input")

"""
Conclusión 
El manejo de strings es esencial en Python porque permite recibir, procesar y mostrar 
información de manera clara y organizada.
Métodos como lower() y strip() ayudan a convertir el texto a minúsculas y eliminar 
espacios innecesarios, mientras que split() y join() permiten separar y unir cadenas.
Las validaciones permiten detectar datos incorrectos o incompletos antes de procesarlos,
evitando errores y la entrada de información innecesaria.
También aprendí que los strings son inmutables, por lo que sus métodos generan nuevas 
cadenas en lugar de modificar directamente la original.
Finalmente, los slices permiten extraer partes específicas de una cadena mediante índices,
facilitando el análisis y la manipulación del texto.
"""
"""
Referencias
1) Python Software Foundation. Built-in Types: Text Sequence Type — str.
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str 
2) Python Software Foundation. An Informal Introduction to Python. 
https://docs.python.org/3/tutorial/introduction.html 
3) Google for Developers. Python Strings.
https://developers.google.com/edu/python/strings 
4) OWASP Foundation. Input Validation Cheat Sheet.
https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
5) Python Software Foundation. String Methods.
https://docs.python.org/3/library/stdtypes.html
"""