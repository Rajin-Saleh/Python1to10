'''
You received a username with messy spaces and inconsistent casing. Clean the string so it is "tidy" and capitalize the first letter of each name.
'''

name = input("Enter your name: ")
exprop_name = name.strip()
prop_name = exprop_name.title()

print(f"You name is {prop_name}.")