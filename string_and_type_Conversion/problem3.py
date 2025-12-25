'''
You have a principal amount and an interest rate as strings. Convert them to floats, calculate the interest (Principal × Rate), and print a message using an F-string
'''

principal_amount = input("What is your principal amount? ")
interest_rate = input("What is your interest rate? ")
conv1_priAmount = float(principal_amount)
conv2_intRate = float(interest_rate)
total_interest = conv1_priAmount * conv2_intRate

print(f"Your principal amount is {principal_amount} dollar.")
print(f"Your interest rate is {principal_amount} percantage.")
print(f"Your total interest is {total_interest} dollar.")

