# Task 3 : Password Strength Checker

def check_password_strength(password):
    is_long_enough = len(password) >= 8
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    score = sum([is_long_enough, has_lower, has_upper, has_digit])
    
    if score == 4:
        return "STRONG PASSWORD"
    elif score >= 2:
        return "MODERATE PASSSWORD"
    else:
        return "WEAK PASSWORD"

if __name__ == "__main__":
    user_password = input("Enter a password to evaluate: ")
    
    strength = check_password_strength(user_password)
    print(f"Your password strength is: {strength}")