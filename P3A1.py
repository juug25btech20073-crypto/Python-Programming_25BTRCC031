import math


def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C = {(celsius * 9 / 5) + 32:.2f}°F")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5 / 9:.2f}°C")


def area_of_circle():
    radius = float(input("Enter radius of the circle: "))
    print(f"Area of Circle = {math.pi * radius * radius:.2f} sq. units")


def simple_interest():
    principal = float(input("Enter Principal Amount (Rs.): "))
    rate = float(input("Enter Rate of Interest (%): "))
    time = float(input("Enter Time (Years): "))
    print(f"Simple Interest = Rs. {(principal * rate * time) / 100:.2f}")


def main():
    operations = {
        "1": celsius_to_fahrenheit,
        "2": fahrenheit_to_celsius,
        "3": area_of_circle,
        "4": simple_interest
    }

    while True:
        print("\n========== PERSONAL UTILITY TOOL ==========")
        print("1. Celsius to Fahrenheit Conversion")
        print("2. Fahrenheit to Celsius Conversion")
        print("3. Calculate Area of Circle")
        print("4. Calculate Simple Interest")
        print("5. Exit")
        print("===========================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the Personal Utility Toolkit.")
            break

        operation = operations.get(choice)

        if operation:
            operation()
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()