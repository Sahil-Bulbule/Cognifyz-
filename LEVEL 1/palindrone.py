# Task 5 : Palindrome Checker

def is_palindrome(text):
    text = text.lower()  
    return text == text[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")