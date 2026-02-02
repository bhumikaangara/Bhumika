import re
def validate_email(email):
    return bool(re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$', email))
def validate_phone(phone):
    return bool(re.fullmatch(r'^[6-9]\d{9}$', phone))
def validate_password(password):
    return bool(re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))
email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
password = input("Enter Password: ")
if validate_email(email):
    print("Email is valid")
else:
    print("Email is invalid")

if validate_phone(phone):
    print("Phone number is valid")
else:
    print("Phone number is invalid")

if validate_password(password):
    print("Password is strong")
else:
    print("Password is weak")
