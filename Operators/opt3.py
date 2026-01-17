'''
Temperature Safety Monitor
Scenario: A server room sensor reports temperature.
Input: Temperature in Celsius (string).
Logic: Convert to float.
If temp > 35.0: "Status: CRITICAL - Cooling required."
Else if temp > 25.0: "Status: WARNING - Monitor closely."
Else: "Status: OK."
Goal: Practice elif chains...
'''

print("\n----- Temperature Safety Monitor -----\n")
try:
 temp = float(input("Enter the temperature in Celcius: "))
 if temp >35.0:
    print("Status: CRITICAL - Cooling required.")
 elif temp > 25.0:
    print("Status: WARNING - Monitor closely.")
 elif temp < -50:
    print("Status: Deadly Outside. Stay inside")
 elif temp < 0:
    print("Status: Sevear Cold Outside.")
 else:
    print("Status: OK.")
except ValueError:
    print("Error: Please enter a valid number.")