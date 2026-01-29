import logging

logging.basicConfig( filename="app.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s" )

class NegativeNumberError(Exception): pass

def divide_numbers(a, b): try: if a < 0 or b < 0: raise NegativeNumberError("Negative numbers are not allowed")

    result = a / b

except ZeroDivisionError:
    logging.error("Division by zero error")
    print("Error: Cannot divide by zero")

except NegativeNumberError as e:
    logging.error(e)
    print("Error:", e)

except Exception as e:
    logging.error(e)
    print("Unexpected error occurred")

else:
    print("Result:", result)

finally:
    print("Execution completed")
divide_numbers(10, 0) divide_numbers(-5, 2) divide_numbers(10, 2)

Task 9 – Exception Handling & Logging (Python)
This project demonstrates:

try-except-else-finally blocks
handling multiple exceptions
custom exception creation
logging errors to a file using Python logging module
Files
error_handling.py – main Python script
app.log – log file with error messages
How to Run
Right click on error_handling.py → Run Python File in Terminal
