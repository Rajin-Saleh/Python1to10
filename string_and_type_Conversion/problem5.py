'''
Task: A restaurant bill is $85.50. You want to split it between 4 people.
Store 85.50 as a string.
Store 4 as a string.
Convert both to numbers (use the appropriate type for each).
Calculate the cost per person.
Print: "Each person owes $21.375"
'''


bill = input("What is your total bill? ")
amount = float(bill)
person = input("How many did you eat? ")
people = int(person)
each_owes = amount / people
print(f"So each person owes {each_owes} dollar.")
