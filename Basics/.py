print("Enter your details:-")
firstname = input("What's your first name?")
lastname = input("What's your last name?")
age = input("enter your age:")

print("Enter Your D.O.B :")
date = input("Date:")
month = input("Month:")
year = input("Year:")

print("Review Your Details Below:-")
print(f"Name: {firstname} {lastname}\nAge: {age}")
print(date, month, year, sep="-")
