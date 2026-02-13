print("Welcome to the rollercoaster!")
height = int(input("What is your height cm? "))
age=int(input("what is your age in numbers? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    if age < 12:
        bill = 10
        print("Child tickets price is $10")
    elif age <= 18:
        bill = 15 
        print("Teenagers ticket price is $15")
    else:
        bill = 20
        print("your ticket price is $20")
    
    wants_photo=input("Do you Want a Photo? Y for yes no N for no. ")
    if wants_photo == "Y":
        bill += 3
        print("your ticket price is $23")
    else:
        bill = bill
        print(f"your ticket price ${bill}")



else:
    print("Sorry, you have to grow taller before you can ride.")