import random
from art import logo,vs
from gamedata import data
from clear import clear

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0

print(logo)
game_should_continue = True
compare_b = random.choice(data)


while game_should_continue:
    compare_a = compare_b

    compare_b = (random.choice(data)) 

    while compare_a == compare_b:
        compare_b = random.choice(data)

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}")

    guess = input("who has more followers A or B: ").lower()
    a_followers = compare_a['follower_count'] 
    b_followers = compare_b['follower_count']    

    is_correct = check_answer(guess,a_followers,b_followers)

    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right. Current Score: {score}.")

    else:
        game_should_continue = False
        print(f"You're wrong. Final Score: {score}.")

