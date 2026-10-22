# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
if name.strip() == "":
    print("Invalid name, try again")
    name = input("Enter customer name: ")
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))
if not previous.isdigit() or not (0 <= int(previous) <=100):
    print ("Invalid consumption rate.")
    previous = float(input("Enter previous meter reading"))
if current < previous:
    print ("Invalid rate.")
    current = float(input("Enter current meter reading"))
consumption = current - previous
total_bill = consumption * RATE

print("Customer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
