
# Interactive Calculator and Unit Converter
# InternCircle Project 01


# Conversion factors
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Read a number safely
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Kilometers to miles
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Kilograms to pounds
def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


# Unit conversion menu
def unit_conversion():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            km = read_number("Enter kilometers: ")
            print("Miles:", km_to_miles(km))

        elif choice == "2":
            celsius = read_number("Enter Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == "3":
            kg = read_number("Enter kilograms: ")
            print("Pounds:", kg_to_pounds(kg))

        elif choice == "4":
            break

        else:
            print("Please choose a number from 1 to 4.")


# Main calculator menu
def main():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Convert Units")
        print("6. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        elif choice in ("1", "2", "3", "4"):
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)

            elif choice == "2":
                result = subtract(a, b)

            elif choice == "3":
                result = multiply(a, b)

            else:
                result = divide(a, b)

            print("Result:", result)

        elif choice == "5":
            unit_conversion()

        else:
            print("Please choose a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()
