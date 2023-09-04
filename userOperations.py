import re
import hashlib

# regex patterns for input validation
name_pattern = r"^[a-zA-Z]+$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
phone_pattern = r"^(01)[0125][0-9]{8}$"
date_pattern = r"^\d{4}-\d{2}-\d{2}$"

#  input validation
def validate_name(name):
    return bool(re.fullmatch(name_pattern, name))

def validate_email(email):
    return bool(re.fullmatch(email_pattern, email))

def validate_password(password):
    return bool(re.fullmatch(password_pattern, password))

def validate_phone(phone):
    return bool(re.fullmatch(phone_pattern, phone))

def validate_date(date):
    return bool(re.fullmatch(date_pattern, date))


# user registration
def register():
    print("\n---------------Register--------------------\n")
    print("Enter your information to register:")
    first_name = input("First name: ")
    while not validate_name(first_name):
        first_name = input("Invalid input. Please enter a valid first name: ")
    last_name = input("Last name: ")
    while not validate_name(last_name):
        last_name = input("Invalid input. Please enter a valid last name: ")
    email = input("Email: ")
    while not validate_email(email):
        email = input("Invalid email. Please enter a valid email: ")
    password = input("Password (at least 8 characters, one uppercase letter, one lowercase letter, and one digit): ")
    while not validate_password(password):
        password = input("Invalid password. Please enter a valid password: ")
    confirm_password = input("Confirm password: ")
    while confirm_password != password:
        confirm_password = input("Passwords do not match. Please confirm your password: ")
    phone = input("Mobile phone (Egyptian phone numbers only): ")
    while not validate_phone(phone):
        phone = input("Invalid phone number. Please enter a valid Egyptian phone number: ")
    
    # Encrypt password 
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    user_data = f"{first_name}:{last_name}:{email}:{password_hash}:{phone}\n"
    with open("users.txt", "a") as f:
        f.write(user_data)
    print("Registration successful.")

    
# user login
def login():
    print("\n---------------Login--------------------\n")
    email = input("Email: ")
    password = input("Password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with open("users.txt", "r") as f:
        for line in f:
            user_data = line.strip().split(":")
            if email == user_data[2] and password_hash == user_data[3]:
                print("Login successful.")
                return email
    print("Invalid email or password.")
    return None
