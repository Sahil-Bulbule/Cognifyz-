# Task 5 : Word Occurrence Counter

def count_words(filename):
    word_count = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

            for char in ".,!?;:\"'()[]{}":
                text = text.replace(char, "")

            words = text.split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

        print("\nWord Occurrences (Alphabetical Order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")

count_words(r"C:\Users\sahil\OneDrive\Desktop\Cognifyz Tasks\LEVEL 2\sample.txt")