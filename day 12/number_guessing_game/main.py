from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("You are correct. The answer was {answer}.")
    
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    if level == "hard":
        turns = HARD_LEVEL_TURNS

# choosing a random number between 1 and 100
print("Welcome to the guessing game!!! \n I am thinking of a number between 1 and 100.")
answer = randint(1,100)

# make function to check difficulty

# let the user guess the number.

guess = int(input("Make a guess: "))
print("You have 5 attempts remaining to guess the number.")

# function to check user's guess against actual number.

# track the number of turns and reduce by one if incorrect guess.

# a self loop

# if answer is write repeat the game or exit