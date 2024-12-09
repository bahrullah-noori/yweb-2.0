def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Celsius to Kelvin")
    print("3: Fahrenheit to Celsius")
    print("4: Fahrenheit to Kelvin")
    print("5: Kelvin to Celsius")
    print("6: Kelvin to Fahrenheit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice in [1, 2]:
        celsius = float(input("Enter temperature in Celsius: "))
        if choice == 1:
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        else:
            print(f"Temperature in Kelvin: {celsius_to_kelvin(celsius):.2f}")
    elif choice in [3, 4]:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        if choice == 3:
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        else:
            print(f"Temperature in Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
    elif choice in [5, 6]:
        kelvin = float(input("Enter temperature in Kelvin: "))
        if choice == 5:
            print(f"Temperature in Celsius: {kelvin_to_celsius(kelvin):.2f}")
        else:
            print(f"Temperature in Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
    else:
        print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
