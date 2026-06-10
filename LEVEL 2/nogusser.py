# Task 2 : Number Guesser Game

import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    
    try:
        min_val = int(input("Enter the minimum value: "))
        max_val = int(input("Enter the maximum value: "))
        
        if min_val >= max_val:
            print("Error: The minimum value must be less than the maximum value.")
            return
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    secret_number = random.randint(min_val, max_val)
    attempts = 0
    
    print(f"\nI have generated a number between {min_val} and {max_val}. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser()