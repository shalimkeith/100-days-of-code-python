print("Welcome to the rollercoaster!")
height = int(input("What is your height cm? "))
age=int(input("what is your age in numbers? "))

if height >= 120:
    print("you can ride the rollercoaster")
    if age < 12:
        print("your ticket price is $10")
    elif age <= 18:
        print("your ticket price is $19")
    elif age > 94:
        print("this old you still want to ride you must be energetic, your ticket is free to heaven")
    else:
        print("your ticket price is $15")
else:
    print("Sorry, you have to grow older before you can ride.")