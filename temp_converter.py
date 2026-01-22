def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def main():
    """Main program loop"""
    print("=== Temperature Converter ===\n")
    
    while True:
        print("Select conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "7":
            print("Thank you for using the Temperature Converter!")
            break
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.\n")
            continue
        
        try:
            temp = float(input("Enter temperature value: "))
            
            if choice == "1":
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.2f}°F\n")
            elif choice == "2":
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.2f}°C\n")
            elif choice == "3":
                result = celsius_to_kelvin(temp)
                print(f"{temp}°C = {result:.2f}K\n")
            elif choice == "4":
                result = kelvin_to_celsius(temp)
                print(f"{temp}K = {result:.2f}°C\n")
            elif choice == "5":
                result = fahrenheit_to_kelvin(temp)
                print(f"{temp}°F = {result:.2f}K\n")
            elif choice == "6":
                result = kelvin_to_fahrenheit(temp)
                print(f"{temp}K = {result:.2f}°F\n")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")


if __name__ == "__main__":
    main()
