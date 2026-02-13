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
    elif age >= 45 and age <= 55:
        bill = 0
        print("If you are Having a midlife crises you can take a ticket.")
    else:
        bill = 20
        print("Adult ticket price is $20")
    
    wants_photo=input("Do you Want a Photo? Y for yes no N for no. ")
    if wants_photo == "Y":
        bill += 3
        print(f"your ticket price is ${bill}")
    else:
        
        print(f"your ticket price ${bill}")



else:
    print("Sorry, you have to grow taller before you can ride.")