# Task 4 : Fibonacci Sequence Generator

def generate_fibonacci(n):              
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
        
    return fib_sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        
        if num_terms <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            sequence = generate_fibonacci(num_terms)
            print(f"The Fibonacci sequence up to {num_terms} terms is: {sequence}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")