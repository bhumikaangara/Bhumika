# datatypes_demo.py
# Task 2: Variables, Data Types & Type Conversion
# Python Developer Internship

# 1. Declaring variables of different data types
integer_var = 10          # int
float_var = 25.5          # float
string_var = "Python"     # string
boolean_var = True        # boolean

# 2. Printing values and their data types
print("Integer Value:", integer_var, "Type:", type(integer_var))
print("Float Value:", float_var, "Type:", type(float_var))
print("String Value:", string_var, "Type:", type(string_var))
print("Boolean Value:", boolean_var, "Type:", type(boolean_var))

print("-" * 40)

# 3. Arithmetic operations using numeric variables
a = 20
b = 7

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("-" * 40)

# 4. Type conversion: converting string input to int and float
try:
    num_str = "100"

    num_int = int(num_str)      # string to integer
    num_float = float(num_str)  # string to float

    print("String to Integer:", num_int, "Type:", type(num_int))
    print("String to Float:", num_float, "Type:", type(num_float))

except ValueError:
    print("Invalid conversion! Cannot convert string to number.")

print("-" * 40)

# 5. Handling invalid input using error handling
try:
    invalid_str = "abc"
    result = int(invalid_str)   # This will cause error
except ValueError:
    print("Error: Cannot convert 'abc' to integer")

print("-" * 40)

# 6. Concatenating strings and numbers properly
age = 21

# Using type casting
message = "My age is " + str(age)
print(message)

print("-" * 40)

# 7. Demonstrating dynamic typing
x = 50
print("x =", x, "Type:", type(x))

x = 50.75
print("x =", x, "Type:", type(x))

x = "Dynamic Typing in Python"
print("x =", x, "Type:", type(x))

print("-" * 40)

# Program completed
print("Task 2 completed successfully!")
