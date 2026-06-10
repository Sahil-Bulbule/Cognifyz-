# Task 2 : Temperature Conversion

temp = float(input("Enter temperature: "))
unit = input("Convert to (C/F): ").upper()

if unit == "C":
    celsius = (temp - 32) * 5 / 9
    print(f"Temperature in Celsius: {celsius:.2f}°C")

elif unit == "F":
    fahrenheit = (temp * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

else:
    print("Invalid unit! Please enter C or F.")