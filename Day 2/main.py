print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
total_people = float(input("How many people to split the bill? "))
percentage_tip = float(input("What percentage tip would like to give? 10, 12 or 15? "))
tip = (total_bill*percentage_tip)/100
individual_amount = (total_bill+tip)/total_people
print("{:.2f}".format(individual_amount))
