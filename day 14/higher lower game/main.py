import random
from art import logo,vs
from gamedata import data

score = 0

print(logo)
compare_a = (random.choice(data))

compare_b = (random.choice(data)) 

while compare_a == compare_b:
    compare_b = random.choice(data)

print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}")
print(vs)
print(f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}")

guess = input("who has more followers A or B: ").lower()
a_followers = compare_a['follower_count'] 
b_followers = compare_b['follower_count']    

if ( guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers):
    print("you are correct")
else: 
    print("you are wrong")