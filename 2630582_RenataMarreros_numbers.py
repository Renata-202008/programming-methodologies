# Manejo de números y booleanos en Python
"""
Renata Valeria Marreros Moreno
2630582
IM 1-2
"""
"""
Resumen Ejecutivo
En Python, los tipos de datos `int` y `float` permiten trabajar con números enteros y
decimales, respectivamente. Los valores booleanos, representados por `True` y `False`,
se obtienen mediante comparaciones y permiten tomar decisiones dentro de un programa. 
La validación de rangos es importante para evitar valores incorrectos, mientras que 
prevenir la división entre cero ayuda a evitar errores durante la ejecución. 
En este documento se describe cada problema, sus entradas y salidas, así como las 
validaciones aplicadas. Además, se demuestra el uso de enteros, números decimales y 
valores booleanos para realizar operaciones, evaluar condiciones y controlar el 
funcionamiento de los programas.

"""
# Problem 1: Temperature converter and range flag
# Description:
# Convert Celsius to Fahrenheit and Kelvin.
# Determine whether the temperature is high (>= 30.0 °C).

# Inputs:
# temp_c (float): Temperature in Celsius.

# Outputs:
# Fahrenheit: <temp_f>
# Kelvin: <temp_k>
# High temperature: true or false

# Validations:
# - The input must be a valid number.
# - The temperature in Kelvin cannot be below 0.0.

# Test Cases:
# 1. Normal: 25 -> Fahrenheit: 77.0, Kelvin: 298.15
# 2. Boundary: 30 -> High temperature: true
# 3. Error: -300 -> Error: invalid temperature

temp_input = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_input)

    # Convert Celsius to Kelvin
    temp_k = temp_c + 273.15

    # Validate the temperature
    if temp_k < 0.0:
        print("Error: invalid temperature")

    else:
        # Convert Celsius to Fahrenheit
        temp_f = temp_c * 9 / 5 + 32

        # Determine whether the temperature is high
        is_high_temperature = temp_c >= 30.0

        # Display the results
        print(f"Fahrenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High temperature: {str(is_high_temperature).lower()}")

except ValueError:
    print("Error: invalid input")

# Problem 2: Work hours and overtime payment
# Description:
# Calculate a worker's weekly pay, including overtime.
# Regular hours are paid at the normal rate.
# Overtime hours are paid at 150% of the normal rate.

# Inputs:
# hours_worked (float): Hours worked during the week.
# hourly_rate (float): Payment per hour.

# Outputs:
# Regular pay, overtime pay, total pay, and overtime status.

# Validations:
# - hours_worked must be greater than or equal to zero.
# - hourly_rate must be greater than zero.

# Test Cases:
# 1. Normal: 35 hours, rate 100
# 2. Boundary: 40 hours, rate 100
# 3. Error: -5 hours, rate 100

hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_input)
    hourly_rate = float(rate_input)

    # Validate the inputs
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")

    else:
        # Calculate regular and overtime hours
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        # Calculate payments
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        # Determine overtime status
        has_overtime = hours_worked > 40

        # Display the results
        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")

except ValueError:
    print("Error: invalid input")

#  Problem 3: Discount eligibility with booleans
# Description:
# Determine whether a customer qualifies for a 10% discount.
# Eligibility depends on student status, senior status,
# or a purchase total of at least 1000.0.

# Inputs:
# purchase_total (float): Total purchase amount.
# is_student_text (string): "YES" or "NO".
# is_senior_text (string): "YES" or "NO".

# Outputs:
# Discount eligible: true or false
# Final total: <final_total>

# Validations:
# - purchase_total must be greater than or equal to 0.
# - Student and senior responses must be "YES" or "NO".

# Test Cases:
# 1. Normal: 500, YES, NO -> 10% discount
# 2. Boundary: 1000, NO, NO -> 10% discount
# 3. Error: -50, YES, NO -> Error: invalid input

purchase_input = input("Enter purchase total: ")
is_student_text = input("Is the customer a student? (YES/NO): ")
is_senior_text = input("Is the customer a senior? (YES/NO): ")

try:
    purchase_total = float(purchase_input)

    # Normalize text inputs
    is_student_text = is_student_text.strip().upper()
    is_senior_text = is_senior_text.strip().upper()

    # Validate all inputs
    if (
        purchase_total < 0
        or is_student_text not in ("YES", "NO")
        or is_senior_text not in ("YES", "NO")
    ):
        print("Error: invalid input")

    else:
        # Convert text responses to boolean values
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        # Determine discount eligibility
        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        # Calculate the final total
        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        # Display the results
        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total:.2f}")

except ValueError:
    print("Error: invalid input")

# Problem 4: Basic statistics of three integers
# Description:
# Read three integers and calculate their sum, average, maximum,
# minimum, and whether all three numbers are even.

# Inputs:
# n1 (int): First integer.
# n2 (int): Second integer.
# n3 (int): Third integer.

# Outputs:
# Sum: <sum_value>
# Average: <average_value>
# Max: <max_value>
# Min: <min_value>
# All even: true|false

# Validations:
# - All three inputs must be valid integers.
# - Negative numbers are allowed.

# Test Cases:
# 1. Normal: 2, 4, 6
#    Sum: 12, Average: 4.0, Max: 6, Min: 2, All even: true
# 2. Boundary: -3, 0, 5
#    Sum: 2, Average: 0.666..., Max: 5, Min: -3, All even: false
# 3. Error: "abc", 2, 4
#    Expected output: Error: invalid input

try:
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))
    n3 = int(input("Enter the third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        (n1 % 2 == 0)
        and (n2 % 2 == 0)
        and (n3 % 2 == 0)
    )

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

except ValueError:
    print("Error: invalid input")

# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Determine whether a person is eligible for a loan based on monthly income, monthly debt, and credit score.

# Inputs:
# monthly_income (float): The person's monthly income.
# monthly_debt (float): The person's monthly debt payments.
# credit_score (int): The person's credit score.

# Outputs:
# Debt ratio: <debt_ratio>
# Eligible: true|false

# Validations:
# - monthly_income must be greater than 0.0.
# - monthly_debt must be greater than or equal to 0.0.
# - credit_score must be greater than or equal to 0.
# - All inputs must have valid numeric formats.

# Test Cases:
# 1. Normal: Income = 10000, Debt = 3000, Score = 700
#    Debt ratio: 0.3, Eligible: true
# 2. Boundary: Income = 8000, Debt = 3200, Score = 650
#    Debt ratio: 0.4, Eligible: true
# 3. Error: Income = 0, Debt = 1000, Score = 700
#    Expected output: Error: invalid input

income_input = input("Enter monthly income: ")
debt_input = input("Enter monthly debt: ")
credit_input = input("Enter credit score: ")

try:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(credit_input)

    if (
        monthly_income <= 0.0
        or monthly_debt < 0.0
        or credit_score < 0
    ):
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")

except ValueError:
    print("Error: invalid input")

# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# Determine whether a person is eligible for a loan based on
# monthly income, monthly debt, and credit score.

# Inputs:
# monthly_income (float): The person's monthly income.
# monthly_debt (float): The person's monthly debt payments.
# credit_score (int): The person's credit score.

# Outputs:
# Debt ratio: <debt_ratio>
# Eligible: true|false

# Validations:
# - monthly_income must be greater than 0.0.
# - monthly_debt must be greater than or equal to 0.0.
# - credit_score must be greater than or equal to 0.
# - All inputs must have valid numeric formats.

# Test Cases:
# 1. Normal: Income = 10000, Debt = 3000, Score = 700
#    Debt ratio: 0.3, Eligible: true
# 2. Boundary: Income = 8000, Debt = 3200, Score = 650
#    Debt ratio: 0.4, Eligible: true
# 3. Error: Income = 0, Debt = 1000, Score = 700
#    Expected output: Error: invalid input

income_input = input("Enter monthly income: ")
debt_input = input("Enter monthly debt: ")
credit_input = input("Enter credit score: ")

try:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(credit_input)

    if (
        monthly_income <= 0.0
        or monthly_debt < 0.0
        or credit_score < 0
    ):
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")

except ValueError:
    print("Error: invalid input")

"""
Conclusión 
El uso de enteros y flotantes permite realizar cálculos precisos en diferentes 
situaciones. Las comparaciones generan valores booleanos que facilitan la toma 
de decisiones mediante estructuras como `if`. Validar rangos y evitar divisiones 
entre cero es fundamental para prevenir errores. Además, las condiciones combinadas 
con `and`, `or` y `not` permiten evaluar varios criterios de manera eficiente. 
Estos conocimientos son útiles para desarrollar programas aplicados a situaciones 
reales, como el cálculo de nóminas, descuentos y préstamos.
"""
"""
Referencias
1) Python Software Foundation. Built-in Types: Numeric Types.
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
2) Python Software Foundation. Boolean Type - bool.
https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
3) Python Software Foundation. Expressions: Operators and Comparisons.
https://docs.python.org/3/reference/expressions.html
4) Python Software Foundation. An Informal Introduction to Python.
https://docs.python.org/3/tutorial/introduction.html
5) W3Schools. Python Operators.
https://www.w3schools.com/python/python_operators.asp
"""