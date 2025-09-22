age = input("what is your current age: ")

age_as_int = int(age)

total_age = 90

years_left = total_age - age_as_int

months_left = years_left * 12

weeks_left = years_left * 52

days_left = years_left * 365

print(f"you have {years_left} years left, you have {months_left} months left, you have {weeks_left} weeks and you have {days_left} days left.")