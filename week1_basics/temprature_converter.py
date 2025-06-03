def celsius_to_farenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def farenheit_to_celsius(farenheit):
    """Convert Fahrenheit to Celsius."""
    return (farenheit - 32) * 5/9

def main():
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice [1 or 2]: ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        farenheit = celsius_to_farenheit(celsius)
        print(f"{celsius}°C is equal to {farenheit}°F")
    elif choice == '2':
        farenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = farenheit_to_celsius(farenheit)
        print(f"{farenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()