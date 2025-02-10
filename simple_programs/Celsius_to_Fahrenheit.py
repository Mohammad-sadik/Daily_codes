def convert_celsius_to_fahrenheit(c):
    f= c*(9/5) +32
    return f"The temperature in Celsius is {c} & The temperature in Fahrenheit is {f}."
Celsius=int(input("Enter the temperature in Celsius : "))
print(convert_celsius_to_fahrenheit(Celsius))