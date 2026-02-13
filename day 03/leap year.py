year = int(input("Which year do you want to check?"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("this is a leap year.")
else:
    print("this is not a leap year.")
    