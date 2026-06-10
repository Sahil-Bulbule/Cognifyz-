# Task 1 : Guessing Game

import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
          
            if guess < 1 or guess > 100:
                print("Please enter a number strictly between 1 and 100.")
                continue
            
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
    guessing_game()