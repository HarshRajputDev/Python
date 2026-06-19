# This is a simple script to convert temperature from fahrenheit to celsius
start_text = "This script converts temperature from fahrenheit to celsius. (it gives round off value)\n\n"
print(start_text)
fahrenheit = float(input("Enter temperature in fahrenheit: "))
fah_to_cel_1 = (fahrenheit - 32)
fah_to_cel_2 = (fah_to_cel_1 // 1.8)
print(f'Fahrenheit to Celsius:\n {fah_to_cel_2}')
