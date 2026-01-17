'''
The E-commerce Discount Engine
Scenario: A store gives a 10% discount if the purchase is over $500.
Input: Total price (string).
Logic: Convert to float. If price > 500, calculate the new total (price * 0.9).
Output: "Final price: $[amount]" (formatted to 2 decimal places).
Goal: Practice math operators and if/else...
'''
print("----- E-commerce Discount Engine -----\n")
price = float(input("Your purchased amount: "))
if price > 500:
    discount = price * 0.1
    total_price = price - discount
    print(f"Discount 10%: ${discount:.2f}")
    print(f"Final price: ${total_price:.2f}")
else:
    print(f"Your total amount is {price:.2f}")