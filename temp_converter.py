def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("\nChoose conversion (1-4): ")
    temp = float(input("Enter temperature: "))
    
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()