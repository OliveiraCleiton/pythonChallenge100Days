# Pizza Order Practice
print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? ( S / M / L) ")
pepperoni = input("Do you want pepperoni on your pizza? ( Y / N ) ")
extra_chesse = input("Do you want extra cheese ( Y / N ) ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_chesse == "Y":
    bill += 1

print(f"Your final bill is: {bill}")