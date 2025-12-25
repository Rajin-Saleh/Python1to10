'''
Create three variables: one string, one integer, and one float. Use the type() function and print() to show the data type of each variable. Add a multi-line comment at the top explaining what the script does.
'''


exp1 = input("Guess your favorite food! ")
exp2 = int(input("What is your birth year? "))
exp3 = float(input("Take any float number! "))

# Taking string as input, printing the content and it type
print(f"Your favorite food is {exp1}. Input Type {type(exp1)}")

# Taking Integer as input, printing the content and it type
print(f"Your birth year is {exp2}. Input Type {type(exp2)}")

# Taking Float as input, printing the content and it type
print(f"Your number is {exp3}. Input Type {type(exp3)}")
