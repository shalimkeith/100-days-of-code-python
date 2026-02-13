import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbol= ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']

print("Welcome to Sk_password_generator ")
nr_letters = int(input("How many letters would like in your password: "))
nr_symbol = int(input("How many symbols would like in your password: "))
nr_numbers = int(input("How many numbers would like in your password: "))
password_list = []
for int in range(1,nr_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1,nr_symbol + 1):
    password_list += random.choice(symbol)
for char in range(1,nr_letters + 1):
    password_list += random.choice(letters)
random.shuffle(password_list)
password=""
for char in password_list:
    password += char
print(password)
