def convert_temperature(celcius):
    fahrenheit = celcius * 9 / 5 + 32
    kelvin = celcius + 273.15
    print(f"Fahrenheit: {fahrenheit}")
    print(f"Kelvin: {kelvin}")


celcius = float(input("Enter a temperature in celcius: "))
convert_temperature(celcius)
