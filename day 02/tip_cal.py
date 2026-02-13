# if the bill was $150 , split between 5 people, with 12% tip.
#Each person should pay (150.00/5) * 1.12
print("Welcome to your personal tip calculator!!")
total_bill = float(input("total amount of bill: "))

bill_split = float(input("bill is splitted into: "))

tip_percentage = float(input("tip paid by the customer: "))

tip_multiplier = 1+(tip_percentage/100)

per_person = (total_bill / bill_split) * tip_multiplier

print(f"each person should pay: ${per_person:.2f}")