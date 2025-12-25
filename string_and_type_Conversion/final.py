'''Mini Project'''

client_name = input("What is your name? ").strip(). title()
hourly_rate = float(input("What is your hourly payment? "))
hour_work = int(input("How many hour did you work? "))
project_name = input("What is your Project name? "). strip().upper()

sub_total = hour_work * hourly_rate
service_fee = sub_total * 0.1
total = sub_total + service_fee

print(f"\n--- INVOICE FOR: {client_name} ---\nProject: {project_name}\nHourly Rate: ${hourly_rate:.2f}\nTotal Hours : {hour_work}\n")
print(f"Subtotal: ${sub_total:.2f}\nService fee (10%): ${service_fee:.2f}\nTOTAL DUE: ${total:.2f}\n--------------------------------------------")

