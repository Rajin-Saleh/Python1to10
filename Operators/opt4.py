'''The "Silent" Data Cleaner
Scenario: A form asks for a phone number.
Input: A phone number string (e.g., " 123 456 7890 ").
Logic: Strip spaces. Check if the length of the string is exactly 10 using len().
Output: If length is 10, print "Valid Number." If not, "Invalid Number."
Goal: Practice len() and string methods in logic...
'''
print("\n---- 'Silent' Data Cleaner ----\n")

number = input("Enter your phone number: ").strip()
cleaned = number.replace(" ","")

if len(cleaned) == 10:
    if cleaned.isdigit():
        print("Valid Number")
    else:
        print("Invalid Number. Must contain only digit.")
    
else:
    print(f"Invalid Number - length is {len(cleaned)},expected exactly 10") 