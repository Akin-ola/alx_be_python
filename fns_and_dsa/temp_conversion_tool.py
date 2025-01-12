FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    to_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {to_celsius}°C")

def convert_to_fahrenheit(celsius):
    to_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {to_fahrenheit}°F")

temperature = int(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if celsius_or_fahrenheit == "F":
    convert_to_celsius(fahrenheit=temperature)
elif celsius_or_fahrenheit == "C":
    convert_to_fahrenheit(celsius=temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")