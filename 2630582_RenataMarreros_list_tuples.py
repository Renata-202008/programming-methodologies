# Manejo de Listas, Tuplas y Diccionarios en Python
"""
Renata Valeria Marreros Moreno
2630582
IM 1-2
"""
"""
Resumen Ejecutivo
Este documento presenta el uso de listas, tuplas y diccionarios en Python 
para organizar y procesar información. 
Se explican sus principales características y diferencias, destacando 
que las listas son mutables, las tuplas son inmutables y los diccionarios 
permiten relacionar claves con valores. Además, se describe cada problema, 
el diseño de sus entradas y salidas y las validaciones aplicadas para evitar 
errores durante la ejecución. Finalmente, se muestra cómo estas estructuras 
de datos pueden utilizarse en situaciones prácticas, como la creación de catálogos, 
el almacenamiento de registros y el cálculo de estadísticas, reforzando los 
conocimientos de programación y la resolución de problemas.
"""
# Problem 1: Shopping list basics (list operations)
# Description:
# Create a product list, add a new product, count the items, and check whether a specific product exists in the list.

# Inputs:
# initial_items_text (string): Initial products separated by commas.
# new_item (string): Product to add to the list.
# search_item (string): Product to search for.

# Outputs:
# Items list: <items_list>
# Total items: <len_list>
# Found item: true|false

# Validations:
# - The initial input cannot be empty.
# - Each product is stripped of extra spaces.
# - The new product and search product cannot be empty.
# - Empty initial product lists are not accepted.

# Test Cases:
# 1. Normal: "apple, banana, orange", "grape", "banana"
#    Total items: 4, Found item: true
# 2. Boundary: "apple", "banana", "pear"
#    Total items: 2, Found item: false
# 3. Error: "   ", "grape", "apple"
#    Expected output: Error: invalid input

initial_items_text = input("Enter initial products separated by commas: ").strip()
new_item = input("Enter a new product: ").strip()
search_item = input("Enter a product to search for: ").strip()

if (
    len(initial_items_text) == 0
    or len(new_item) == 0
    or len(search_item) == 0
):
    print("Error: invalid input")
else:
    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if len(item.strip()) > 0
    ]

    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        items_list.append(new_item)

        len_list = len(items_list)
        is_in_list = search_item in items_list

        print(f"Items list: {items_list}")
        print(f"Total items: {len_list}")
        print(f"Found item: {str(is_in_list).lower()}")

# Problem 2: Points and distances with tuples
# Description:
# Create a product list, add a new product, count the items, and check whether a specific product exists in the list.

# Inputs:
# initial_items_text (string): Initial products separated by commas.
# new_item (string): Product to add to the list.
# search_item (string): Product to search for.

# Outputs:
# Items list: <items_list>
# Total items: <len_list>
# Found item: true|false

# Validations:
# - The initial input cannot be empty.
# - Each product is stripped of extra spaces.
# - The new product and search product cannot be empty.
# - Empty initial product lists are not accepted.

# Test Cases:
# 1. Normal: "apple, banana, orange", "grape", "banana"
#    Total items: 4, Found item: true
# 2. Boundary: "apple", "banana", "pear"
#    Total items: 2, Found item: false
# 3. Error: "   ", "grape", "apple"
#    Expected output: Error: invalid input

initial_items_text = input("Enter initial products separated by commas: ").strip()
new_item = input("Enter a new product: ").strip()
search_item = input("Enter a product to search for: ").strip()

if (
    len(initial_items_text) == 0
    or len(new_item) == 0
    or len(search_item) == 0
):
    print("Error: invalid input")
else:
    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if len(item.strip()) > 0
    ]

    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        items_list.append(new_item)

        len_list = len(items_list)
        is_in_list = search_item in items_list

        print(f"Items list: {items_list}")
        print(f"Total items: {len_list}")
        print(f"Found item: {str(is_in_list).lower()}")

# Problem 3: Product catalog with dictionary
# Description:
# Manage a product catalog using a dictionary and calculate the total purchase price when a product exists.

# Inputs:
# product_name (string): The name of the product to purchase.
# quantity (int): The quantity of products to purchase.

# Outputs:
# Unit price: <unit_price>
# Quantity: <quantity>
# Total: <total_price>
# Error: product not found
# Error: invalid input

# Validations:
# - The product name cannot be empty.
# - The quantity must be a valid integer greater than zero.
# - The product must exist in the dictionary.

# Test Cases:
# 1. Normal: Product = "apple", Quantity = 3
#    Unit price: 10.00, Quantity: 3, Total: 30.00
# 2. Boundary: Product = "banana", Quantity = 1
#    Unit price: 5.00, Quantity: 1, Total: 5.00
# 3. Error: Product = "orange", Quantity = 2
#    Expected output: Error: product not found

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "milk": 25.0,
    "bread": 18.0
}

product_name = input("Enter the product name: ").strip().lower()
quantity_input = input("Enter the quantity: ")

if len(product_name) == 0:
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_input)

        if quantity <= 0:
            print("Error: invalid input")
        elif product_name not in product_prices:
            print("Error: product not found")
        else:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity

            print(f"Unit price: {unit_price:.2f}")
            print(f"Quantity: {quantity}")
            print(f"Total: {total_price:.2f}")

    except ValueError:
        print("Error: invalid input")

# Problem 4: Student grades with dict and list
# Description:
# Manage student grades using a dictionary and calculate the average and passing status for a selected student.

# Inputs:
# student_name (string): The name of the student.

# Outputs:
# Grades: <grades_list>
# Average: <average>
# Passed: true|false
# Error: student not found

# Validations:
# - The student name cannot be empty.
# - The student must exist in the dictionary.
# - The grades list cannot be empty.

# Test Cases:
# 1. Normal: Student = "Alice", Grades = [90.0, 85.0, 80.0]
#    Average: 85.00, Passed: true
# 2. Boundary: Student = "Bob", Grades = [70.0, 70.0, 70.0]
#    Average: 70.00, Passed: true
# 3. Error: Student = "David"
#    Expected output: Error: student not found

grades = {
    "Alice": [90.0, 85.0, 80.0],
    "Bob": [70.0, 70.0, 70.0],
    "Charlie": [60.0, 65.0, 68.0]
}

student_name = input("Enter the student name: ").strip()

if len(student_name) == 0:
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    grades_list = grades[student_name]

    if len(grades_list) == 0:
        print("Error: no grades available")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0

        print(f"Grades: {grades_list}")
        print(f"Average: {average:.2f}")
        print(f"Passed: {str(is_passed).lower()}")

# Problem 5: Word frequency counter (list + dict)
# Description:
# Count the frequency of each word in a sentence using a list and a dictionary. The sentence is converted to lowercase, and simple punctuation marks are removed.

# Inputs:
# sentence (string): A sentence entered by the user.

# Outputs:
# Words list: <words_list>
# Frequencies: <freq_dict>
# Most common word: <word>

# Validations:
# - The sentence cannot be empty after removing surrounding spaces.
# - The list of words must not be empty.
# - Simple punctuation marks are removed using replace().

# Test Cases:
# 1. Normal:
#    Input: "Python is easy and Python is useful"
#    Expected most common word: "python" or "is"
# 2. Boundary:
#    Input: "Hello"
#    Expected output:
#    Words list: ['hello']
#    Frequencies: {'hello': 1}
#    Most common word: hello
# 3. Error:
#    Input: "   "
#    Expected output: Error: invalid input

sentence = input("Enter a sentence: ").strip()

if len(sentence) == 0:
    print("Error: invalid input")
else:
    sentence = sentence.lower()

    # Remove simple punctuation marks.
    punctuation_marks = [".", ",", ";", ":", "!", "?", "(", ")", '"', "'"]

    for mark in punctuation_marks:
        sentence = sentence.replace(mark, "")

    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        # Count the frequency of each word.
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # Find the word with the highest frequency.
        most_common_word = ""
        highest_frequency = 0

        for word in freq_dict:
            if freq_dict[word] > highest_frequency:
                highest_frequency = freq_dict[word]
                most_common_word = word

        print(f"Words list: {words_list}")
        print(f"Frequencies: {freq_dict}")
        print(f"Most common word: {most_common_word}")

# Problem 6: Simple contact book (dictionary CRUD)
# Description:
# Manage a contact book using a dictionary. Each contact name is a key, and its phone number is the corresponding value. The program can add, search for, or delete contacts.

# Inputs:
# action_text (string): The operation to perform: ADD, SEARCH, or DELETE.
# name (string): The contact name.
# phone (string): The contact phone number, required only for ADD.

# Outputs:
# ADD: Contact saved: <name>, <phone>
# SEARCH: Phone: <phone>
# DELETE: Contact deleted: <name>
# Error: contact not found
# Error: invalid input

# Validations:
# - Convert the action to uppercase.
# - The action must be ADD, SEARCH, or DELETE.
# - The contact name cannot be empty.
# - The phone number cannot be empty when adding a contact.

# Test Cases:
# 1. Normal:
#    Action: ADD, Name: "David", Phone: "5551234567"
#    Expected output: Contact saved: David, 5551234567
# 2. Boundary:
#    Action: SEARCH, Name: "Alice"
#    Expected output: Phone: 1234567890
# 3. Error:
#    Action: SEARCH, Name: "Unknown"
#    Expected output: Error: contact not found

contacts = {
    "Alice": "1234567890",
    "Bob": "0987654321",
    "Charlie": "5551112233"
}

action_text = input("Enter an action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")

else:
    name = input("Enter the contact name: ").strip()

    if len(name) == 0:
        print("Error: invalid input")

    elif action_text == "ADD":
        phone = input("Enter the phone number: ").strip()

        if len(phone) == 0:
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print(f"Contact saved: {name}, {phone}")

    elif action_text == "SEARCH":
        if name in contacts:
            phone = contacts.get(name)
            print(f"Phone: {phone}")
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")

"""
Conclusión 
Las listas son útiles cuando se necesita almacenar una colección de datos que 
puede cambiar durante la ejecución del programa.
Permiten agregar elementos con append() y eliminar elementos con remove() o pop()
, ofreciendo flexibilidad para organizar información.
Las tuplas son convenientes para guardar datos que no deben modificarse, como 
coordenadas o registros fijos.
Los diccionarios facilitan la búsqueda de información mediante claves, permitiendo 
acceder rápidamente a los valores asociados.
Al combinar estas estructuras, es posible organizar datos de manera más eficiente 
según las necesidades de cada problema.
Un patrón común es utilizar un diccionario de listas para agrupar varios elementos 
bajo una misma clave.
En conclusión, elegir la estructura adecuada mejora la organización, el manejo y la 
comprensión de los datos en Python.
"""
"""
Referencias
# References:
1) Python Software Foundation. Data Structures - Lists, Tuples, and Dictionaries.
https://docs.python.org/3/tutorial/datastructures.html
2) Python Software Foundation. Built-in Types - Lists and Tuples.
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple
3) Python Software Foundation. Mapping Types - Dictionary (dict).
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
4) Python Software Foundation. An Informal Introduction to Python.
https://docs.python.org/3/tutorial/introduction.html
5) Python Software Foundation. The Python Tutorial.
https://docs.python.org/3/tutorial/
"""