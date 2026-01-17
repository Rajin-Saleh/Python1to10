'''
The Security Gatekeeper (Access Logic)
Scenario: A user wants to enter a restricted area.
Input: User's age (string) and their "Is Employee" status (string like "yes" or "no").
Logic: Convert age to int. If the user is 18 or older AND "Is Employee" is "yes", print "Access Granted." Otherwise, print "Access Denied."
Goal: Practice and operators with type conversion...
'''

isEmployee = input("Do you work here? Yes or No: ").strip().title()

if isEmployee == "Yes":
    age = int(input("What is your age? "))
    if age >= 18 :
        print("You are allowed.")
    else:
        print("You are too young for access")
elif isEmployee == "No":
    print("You do not work here. Bye")
else:
    print("Invalid input")
    