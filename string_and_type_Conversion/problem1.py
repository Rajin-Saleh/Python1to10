'''
Create a variable for a user's age as a string. Convert it to an integer, multiply it by 365, and print the result. Use comments to explain why you are converting the type.
'''



age = input("What ais your age? ")
conv = int(age)
days = conv * 365
print(f"You are {days} days or {conv} years old.")