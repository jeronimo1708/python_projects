# Program asks for total bill, then will ask for percentage to be tipped.
# Finally it will ask how many people will split the bill.
# Output should only contain decimals upto 2 digits.

print("Welcome to the tip calculator")
total_bill = int(input("What is the total bill?\n"))
percent_tip = int(input("What percent would you like to tip?\n"))
total_number_of_people = int(input("How many people to split the bill?\n"))
cost_per_person = (total_bill + (total_bill * (percent_tip / 100))) / total_number_of_people
print(f"Each person pays {cost_per_person}")