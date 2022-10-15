# Welcome Message
print("Welcome to the tip calculator")
# Asking and storing the amount of the bill
bill = float(input(print("What is the amount of of the bill")))
# Asking and storing the tip percentage
tipPercent = int(input(print("What percentage tip do you want to leave?")))
# checking to make sure the tip is at least 10%
if tipPercent < 10:
  print("Waiters need to pay rent to. Please leave a bigger tip")
# Getting the amount of people that ate
people = int(input(print("How many people ate?")))
# calculating the total bill
totalBill = tipPercent / 100 * bill + bill
# spliting the bill between everyone
eachPersonOwes = totalBill / people
# rounding the split bill to 2 decimal places
finalAmount = round(eachPersonOwes, 2)
# limiting the finalAmount to 2 decimal places
finalAmount = "{:.2F}".format(eachPersonOwes)
# Displaying the amount each person owes
print(f"Each person owes {finalAmount}")