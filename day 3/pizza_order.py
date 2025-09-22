print("welcome to Keith's pizza!")
size = input("what size pizza you want? s,m,l,xl")
add_pepperoni = input("do you want pepperoni with it? y,n")
add_extra_cheese = input("do you want to add extra cheese with it? y,n")

bill = 0 

if size == "s":
    bill += 15
    
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    bill += 30

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if add_extra_cheese == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3


print(f"Your final bill ${bill}")