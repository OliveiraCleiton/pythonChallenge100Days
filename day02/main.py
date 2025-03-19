# day 02, project Tip of Calculator

print("Welcome to the tip Calculator!")
bill = float(input("What's was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
payers = int(input("How much people split the bill? "))
percentage = tip / 100
bill =  bill + bill * percentage
total_each_person = round(bill / payers, 2)
print(f"Each person should pay: {total_each_person}")