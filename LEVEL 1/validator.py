# Task 3 : Email Validator

def is_valid_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")